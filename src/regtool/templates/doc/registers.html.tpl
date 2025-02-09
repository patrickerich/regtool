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
    </style>
</head>
<body>
    <h1>${name.upper()} Register Documentation</h1>
    <p>${desc}</p>

    <h2>Register Map</h2>
    <table>
        <tr><th>Offset</th><th>Name</th><th>Description</th></tr>
% for register in registers:
        <tr>
            <td>0x${"%x" % register.offset}</td>
            <td>${register.name}</td>
            <td>${register.desc}</td>
        </tr>
% endfor
    </table>

    <h2>Memory Regions</h2>
    <table>
        <tr><th>Offset</th><th>Name</th><th>Size</th><th>Width</th><th>Description</th></tr>
% for memory in memories:
        <tr>
            <td>0x${"%x" % memory.offset}</td>
            <td>${memory.name}</td>
            <td>${memory.size}</td>
            <td>${memory.width}</td>
            <td>${memory.desc}</td>
        </tr>
% endfor
    </table>

    <h2>Register Details</h2>
% for register in registers:
    <h3>${register.name}${"[%d]" % register.array_size if register.get('is_array', False) else ""} 
    (0x${"%x" % register.offset}${"-%x" % (register.offset + (register.array_size - 1) * register.array_stride) if register.get('is_array', False) else ""})</h3>
    <p>${register.desc}</p>
% if register.get('is_array', False):
    <p>Array of ${register.array_size} registers, ${register.array_stride}-byte aligned</p>
% endif
    <table>
        <tr><th>Bits</th><th>Name</th><th>Access</th><th>Description</th></tr>
% for field in register.fields:
        <tr>
            <td>${field.msb}${':' + str(field.lsb) if field.msb != field.lsb else ''}</td>
            <td>${field.name}</td>
            <td>${register.swaccess}</td>
            <td>${field.desc}</td>
        </tr>
% endfor
    </table>
% endfor
</body>
</html>