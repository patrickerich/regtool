# ${name.upper()} Register Documentation

${desc}

## Register Map

| Offset | Name | Description | Reset Value | Type | Access | HW Access | Aliases |
|--------|------|-------------|-------------|------|---------|-----------|----------|
% for register in registers:
| 0x${"%x" % register.offset} | ${register.name} | ${register.desc} | 0x${"%x" % register.reset_value} | ${register.is_external and 'External' or 'Internal'} | ${register.swaccess} | ${register.hwaccess} | ${register.aliases or '-'} |
% endfor

## Register Details

% for register in registers:
### ${register.name} (0x${"%x" % register.offset})
${register.desc}

Type: ${register.is_external and 'External' or 'Internal'}
Reset Value: 0x${"%x" % register.reset_value}
Software Access: ${register.swaccess}
Hardware Access: ${register.hwaccess}

| Bits | Name | Access | Reset | HW Access | Description |
|------|------|--------|--------|------------|-------------|
% for field in register.fields:
| ${field.msb}${':' + str(field.lsb) if field.msb != field.lsb else ''} | ${field.name} | ${register.swaccess} | 0x${"%x" % field.reset} | ${register.hwaccess} | ${field.desc} |
% endfor

% endfor
