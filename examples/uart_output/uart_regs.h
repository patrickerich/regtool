#ifndef UART_REGS_H
#define UART_REGS_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

// Register block configuration
#define UART_REG_AW 32
#define UART_REG_DW 32

// Register offsets and aliases
#define UART_ctrl_OFFSET 0x0
#define UART_status_OFFSET 0x4
#define UART_data_OFFSET 0x8

// Register field masks and shifts
#define UART_ctrl_en_MASK 0x1
#define UART_ctrl_en_SHIFT 0
#define UART_ctrl_en_RESET 0x0
#define UART_ctrl_en_WIDTH 1
#define UART_ctrl_parity_MASK 0x2
#define UART_ctrl_parity_SHIFT 1
#define UART_ctrl_parity_RESET 0x0
#define UART_ctrl_parity_WIDTH 1

#define UART_status_txfull_MASK 0x1
#define UART_status_txfull_SHIFT 0
#define UART_status_txfull_RESET 0x0
#define UART_status_txfull_WIDTH 1
#define UART_status_rxempty_MASK 0x2
#define UART_status_rxempty_SHIFT 1
#define UART_status_rxempty_RESET 0x0
#define UART_status_rxempty_WIDTH 1

#define UART_data_value_MASK 0xff
#define UART_data_value_SHIFT 0
#define UART_data_value_RESET 0x0
#define UART_data_value_WIDTH 8


// Register access types
#define UART_ctrl_ACCESS_TYPE "rw"
#define UART_ctrl_HW_ACCESS "none"
#define UART_ctrl_IS_EXTERNAL 0
#define UART_status_ACCESS_TYPE "rw"
#define UART_status_HW_ACCESS "none"
#define UART_status_IS_EXTERNAL 0
#define UART_data_ACCESS_TYPE "rw"
#define UART_data_HW_ACCESS "none"
#define UART_data_IS_EXTERNAL 0

// Register access macros
#define REG_READ32(addr) (*(volatile uint32_t *)(addr))
#define REG_WRITE32(addr, value) (*(volatile uint32_t *)(addr) = (uint32_t)(value))

// Field access macros
#define GET_FIELD(reg, mask, shift) (((reg) >> (shift)) & (mask))
#define SET_FIELD(reg, mask, shift, value) (((reg) & ~((mask) << (shift))) | (((value) & (mask)) << (shift)))

// Register structure
typedef struct uart_regs {
    volatile uint32_t ctrl;  /* Control Register */
    volatile uint32_t status;  /* Status Register */
    volatile uint32_t data;  /* Data Register */
} uart_regs_t;

// Register reset values
#define UART_ctrl_RESETVALUE 0x0
#define UART_status_RESETVALUE 0x0
#define UART_data_RESETVALUE 0x0

#ifdef __cplusplus
}
#endif

#endif  // UART_REGS_H
