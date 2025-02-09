<!DOCTYPE html>
<html>
<head>
    <title>${name.upper()} Register Documentation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f5f5f5; }
        h1, h2, h3 { color: #333; }
        .reg-details { margin: 10px 0; }
        .field-table { margin-top: 15px; }
    </style>
</head>
<body>
    <h1>${name.upper()} Register Documentation</h1>
    <p>${desc}</p>

    <h2>Register Map</h2>
    <table>
        <tr>
            <th>Offset</th>
            <th>Name</th>
            <th>Description</th>
            <th>Reset Value</th>
            <th>Type</th>
            <th>Access</th>
            <th>HW Access</th>
            <th>Aliases</th>
        </tr>
% for register in registers:
        <tr>
% if register.is_array:
            <td>0x${"%x" % register.offset} + i×0x${"%x" % register.array_stride}</td>
            <td>${register.name}[${register.array_size}]</td>
% else:
            <td>0x${"%x" % register.offset}</td>
            <td>${register.name}</td>
% endif
            <td>${register.desc}</td>
            <td>0x${"%x" % register.reset_value}</td>
            <td>${register.is_array and 'Array' or (register.is_external and 'External' or 'Internal')}</td>
            <td>${register.swaccess}</td>
            <td>${register.hwaccess}</td>
            <td>${', '.join(['0x%x' % a for a in register.get('aliases', [])])}</td>
        </tr>
% endfor
    </table>

    <h2>Register Details</h2>
% for register in registers:
    <h3>${register.name} ${register.is_array and f'[{register.array_size}]' or ''} (0x${"%x" % register.offset})</h3>
    <div class="reg-details">
        <p>${register.desc}</p>
        <p><strong>Type:</strong> ${register.is_external and 'External' or 'Internal'}</p>
        <p><strong>Reset Value:</strong> 0x${"%x" % register.reset_value}</p>
        <p><strong>Software Access:</strong> ${register.swaccess}</p>
        <p><strong>Hardware Access:</strong> ${register.hwaccess}</p>
% if register.get('aliases', []):
        <p><strong>Aliases:</strong> ${', '.join(['0x%x' % a for a in register.aliases])}</p>
% endif
% if register.is_array:
        <p><strong>Array Size:</strong> ${register.array_size}</p>
        <p><strong>Array Stride:</strong> 0x${"%x" % register.array_stride}</p>
% endif
    </div>

    <table class="field-table">
        <tr>
            <th>Bits</th>
            <th>Name</th>
            <th>Access</th>
            <th>Reset</th>
            <th>HW Access</th>
            <th>Description</th>
        </tr>
% for field in register.fields:
        <tr>
            <td>${field.msb}${':' + str(field.lsb) if field.msb != field.lsb else ''}</td>
            <td>${field.name}</td>
            <td>${register.swaccess}</td>
            <td>0x${"%x" % field.reset}</td>
            <td>${register.hwaccess}</td>
            <td>${field.desc}</td>
        </tr>
% endfor
    </table>
% endfor
</body>
</html>