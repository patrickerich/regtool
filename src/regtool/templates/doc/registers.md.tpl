# ${name.upper()} Register Documentation

${desc}

## Register Map

| Offset | Name | Description | Reset Value | Type | Access | HW Access | Aliases |
|--------|------|-------------|-------------|------|---------|-----------|----------|
% for register in registers:
% if register.is_array:
| 0x${"%x" % register.offset} + i×0x${"%x" % register.array_stride} | ${register.name}[${register.array_size}] | ${register.desc} | 0x${"%x" % register.reset_value} | Array | ${register.swaccess} | ${register.hwaccess} | ${', '.join(['0x%x' % a for a in register.get('aliases', [])])} |
% else:
| 0x${"%x" % register.offset} | ${register.name} | ${register.desc} | 0x${"%x" % register.reset_value} | ${register.is_external and 'External' or 'Internal'} | ${register.swaccess} | ${register.hwaccess} | ${', '.join(['0x%x' % a for a in register.get('aliases', [])])} |
% endif
% endfor

## Register Details

% for register in registers:
### ${register.name} ${register.is_array and f'[{register.array_size}]' or ''} (0x${"%x" % register.offset})
${register.desc}

Type: ${register.is_external and 'External' or 'Internal'}
Reset Value: 0x${"%x" % register.reset_value}
Software Access: ${register.swaccess}
Hardware Access: ${register.hwaccess}
% if register.get('aliases', []):
Aliases: ${', '.join(['0x%x' % a for a in register.aliases])}
% endif
% if register.is_array:
Array Size: ${register.array_size}
Array Stride: 0x${"%x" % register.array_stride}
% endif

| Bits | Name | Access | Reset | HW Access | Description |
|------|------|--------|--------|------------|-------------|
% for field in register.fields:
| ${field.msb}${':' + str(field.lsb) if field.msb != field.lsb else ''} | ${field.name} | ${register.swaccess} | 0x${"%x" % field.reset} | ${register.hwaccess} | ${field.desc} |
% endfor

% endfor