#ifndef ${name.upper()}_REGS_H
#define ${name.upper()}_REGS_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

// Access type definitions
#define REG_ACCESS_RW   0
#define REG_ACCESS_RO   1
#define REG_ACCESS_WO   2
#define REG_ACCESS_W1C  3
#define REG_ACCESS_W1S  4

// Register types
#define REG_TYPE_INTERNAL 0
#define REG_TYPE_EXTERNAL 1

// Register offsets and types
% for register in registers:
#define ${name.upper()}_${register.name}_OFFSET 0x${"%x" % register.offset}
#define ${name.upper()}_${register.name}_TYPE REG_TYPE_${"EXTERNAL" if register.get('is_external', False) else "INTERNAL"}
#define ${name.upper()}_${register.name}_ACCESS REG_ACCESS_${register.swaccess.upper()}
% endfor

// Memory region definitions
% for memory in memories:
#define ${name.upper()}_${memory.name}_OFFSET 0x${"%x" % memory.offset}
#define ${name.upper()}_${memory.name}_SIZE ${memory.size}
#define ${name.upper()}_${memory.name}_WIDTH ${memory.width}
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

// Memory access macros
#define MEM_READ(addr, width) (*(volatile uint##width##_t *)(addr))
#define MEM_WRITE(addr, width, value) (*(volatile uint##width##_t *)(addr) = (uint##width##_t)(value))

// Array and memory address calculation
#define REG_ARRAY_ADDR(base, array_offset, stride, index) ((base) + (array_offset) + ((index) * (stride)))
#define MEM_ADDR(base, mem_offset, width, index) ((base) + (mem_offset) + ((index) * ((width)/8)))

// Field access macros
#define GET_FIELD(reg, mask, shift) (((reg) >> (shift)) & (mask))
#define SET_FIELD(reg, mask, shift, value) (((reg) & ~((mask) << (shift))) | (((value) & (mask)) << (shift)))

// Register structure
typedef struct ${name}_regs {
% for register in registers:
% if register.get('is_array', False):
    volatile uint32_t ${register.name.lower()}[${register.array_size}];  /* ${register.desc} */
% else:
    volatile uint32_t ${register.name.lower()};  /* ${register.desc} */
% endif
% endfor
% for memory in memories:
    volatile uint${memory.width}_t ${memory.name.lower()}[${memory.size}];  /* ${memory.desc} */
% endfor
} ${name}_regs_t;

#ifdef __cplusplus
}
#endif

#endif  // ${name.upper()}_REGS_H
