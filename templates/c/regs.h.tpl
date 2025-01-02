#ifndef ${name.upper()}_REGS_H
#define ${name.upper()}_REGS_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

// Register offsets
% for register in registers:
#define ${name.upper()}_${register.name}_OFFSET 0x${"%x" % register.offset}
% endfor

// Register field masks and shifts
% for register in registers:
% for field in register.fields:
#define ${name.upper()}_${register.name}_${field.name}_MASK ${hex((1 << field.width) - 1)}
#define ${name.upper()}_${register.name}_${field.name}_SHIFT ${field.lsb}
% endfor

% endfor

// Register access macros
#define REG_READ32(addr) (*(volatile uint32_t *)(addr))
#define REG_WRITE32(addr, value) (*(volatile uint32_t *)(addr) = (uint32_t)(value))

// Field access macros
#define GET_FIELD(reg, mask, shift) (((reg) >> (shift)) & (mask))
#define SET_FIELD(reg, mask, shift, value) (((reg) & ~((mask) << (shift))) | (((value) & (mask)) << (shift)))

// Register structure
typedef struct ${name}_regs {
% for register in registers:
    volatile uint32_t ${register.name.lower()};  /* ${register.desc} */
% endfor
} ${name}_regs_t;

#ifdef __cplusplus
}
#endif

#endif  // ${name.upper()}_REGS_H