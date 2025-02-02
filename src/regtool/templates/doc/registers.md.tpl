# {{ name|upper }} Register Documentation

{{ desc }}

## Register Map

| Offset | Name | Description |
|--------|------|-------------|
{% for register in registers %}
| 0x{{ "%x"|format(register.offset) }} | {{ register.name }} | {{ register.desc }} |
{% endfor %}

## Register Details

{% for register in registers %}
### {{ register.name }} (0x{{ "%x"|format(register.offset) }})
{{ register.desc }}

| Bits | Name | Access | Description |
|------|------|--------|-------------|
{% for field in register.fields %}
| {{ field.msb }}{{ ':' + field.lsb|string if field.msb != field.lsb else '' }} | {{ field.name }} | {{ register.swaccess }} | {{ field.desc }} |
{% endfor %}

{% endfor %}