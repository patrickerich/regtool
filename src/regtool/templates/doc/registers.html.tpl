<!DOCTYPE html>
<html>
<head>
    <title>{{ name|upper }} Register Documentation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f5f5f5; }
        h1, h2, h3 { color: #333; }
    </style>
</head>
<body>
    <h1>{{ name|upper }} Register Documentation</h1>
    <p>{{ desc }}</p>

    <h2>Register Map</h2>
    <table>
        <tr><th>Offset</th><th>Name</th><th>Description</th></tr>
{% for register in registers %}
        <tr>
            <td>0x{{ "%x"|format(register.offset) }}</td>
            <td>{{ register.name }}</td>
            <td>{{ register.desc }}</td>
        </tr>
{% endfor %}
    </table>

    <h2>Register Details</h2>
{% for register in registers %}
    <h3>{{ register.name }} (0x{{ "%x"|format(register.offset) }})</h3>
    <p>{{ register.desc }}</p>
    <table>
        <tr><th>Bits</th><th>Name</th><th>Access</th><th>Description</th></tr>
{% for field in register.fields %}
        <tr>
            <td>{{ field.msb }}{{ ':' + field.lsb|string if field.msb != field.lsb else '' }}</td>
            <td>{{ field.name }}</td>
            <td>{{ register.swaccess }}</td>
            <td>{{ field.desc }}</td>
        </tr>
{% endfor %}
    </table>
{% endfor %}
</body>
</html>