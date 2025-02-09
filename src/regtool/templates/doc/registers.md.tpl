# ${name.upper()} Register Documentation

${desc}

## Register Map

| Offset | Name | Description |
|--------|------|-------------|
% for register in registers:
| 0x${"%x" % register.offset} | ${register.name} | ${register.desc} |
% endfor

## Memory Regions

| Offset | Name | Size | Width | Description |
|--------|------|------|-------|-------------|
% for memory in memories:
| 0x${"%x" % memory.offset} | ${memory.name} | ${memory.size} | ${memory.width} | ${memory.desc} |
% endfor

## Register Details

% for register in registers:
### ${register.name}${"[%d]" % register.array_size if register.get('is_array', False) else ""} (0x${"%x" % register.offset}${"-%x" % (register.offset + (register.array_size - 1) * register.array_stride) if register.get('is_array', False) else ""})
${register.desc}
% if register.get('is_array', False):
Array of ${register.array_size} registers, ${register.array_stride}-byte aligned
% endif

| Bits | Name | Access | Description |
|------|------|--------|-------------|
% for field in register.fields:
| ${field.msb}${':' + str(field.lsb) if field.msb != field.lsb else ''} | ${field.name} | ${register.swaccess} | ${field.desc} |
% endfor

% endfor