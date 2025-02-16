#ifndef ${name.upper()}_REGS_H
#define ${name.upper()}_REGS_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

// Register block configuration
#define ${name.upper()}_REG_AW ${reg_aw}
#define ${name.upper()}_REG_DW ${reg_dw}

// Register offsets and aliases
{% for register in registers %}
{% if register.is_array %}
#define ${name.upper()}_${register.name}_COUNT ${register.array_size}
#define ${name.upper()}_${register.name}_STRIDE 0x${"%x" % register.array_stride}
#define ${name.upper()}_${register.name}_OFFSET(i) (0x${"%x" % register.offset} + (i) * ${name.upper()}_${register.name}_STRIDE)
{% else %}
#define ${name.upper()}_${register.name}_OFFSET 0x${"%x" % register.offset}
{% for idx, alias in enumerate(register.get('aliases', [])) %}
#define ${name.upper()}_${register.name}_ALIAS${idx}_OFFSET 0x${"%x" % alias}
{% endfor %}
{% endif %}
{% endfor %}

// Register field masks and shifts
{% for register in registers %}
{% for field in register.fields %}
#define ${name.upper()}_${register.name}_${field.name}_MASK 0x${"%x" % field.mask}
#define ${name.upper()}_${register.name}_${field.name}_SHIFT ${field.lsb}
#define ${name.upper()}_${register.name}_${field.name}_RESET 0x${"%x" % field.reset}
#define ${name.upper()}_${register.name}_${field.name}_WIDTH ${field.width}
{% endfor %}

{% endfor %}

// Register access types
{% for register in registers %}
#define ${name.upper()}_${register.name}_ACCESS_TYPE "${register.swaccess}"
#define ${name.upper()}_${register.name}_HW_ACCESS "${register.hwaccess}"
#define ${name.upper()}_${register.name}_IS_EXTERNAL ${1 if register.is_external else 0}
{% endfor %}

// Register access macros
#define REG_READ32(addr) (*(volatile uint32_t *)(addr))
#define REG_WRITE32(addr, value) (*(volatile uint32_t *)(addr) = (uint32_t)(value))

// Field access macros
#define GET_FIELD(reg, mask, shift) (((reg) >> (shift)) & (mask))
#define SET_FIELD(reg, mask, shift, value) (((reg) & ~((mask) << (shift))) | (((value) & (mask)) << (shift)))

// Register structure
typedef struct ${name}_regs {
{% for register in registers %}
{% if register.is_array %}
    volatile uint32_t ${register.name.lower()}[${register.array_size}];  /* ${register.desc} */
{% else %}
    volatile uint32_t ${register.name.lower()};  /* ${register.desc} */
{% endif %}
{% endfor %}
} ${name}_regs_t;

// Register reset values
{% for register in registers %}
{% if register.is_array %}
#define ${name.upper()}_${register.name}_RESETVALUE(i) 0x${"%x" % register.reset_value}
{% else %}
#define ${name.upper()}_${register.name}_RESETVALUE 0x${"%x" % register.reset_value}
{% endif %}
{% endfor %}

#ifdef __cplusplus
}
#endif

#endif  // ${name.upper()}_REGS_H
