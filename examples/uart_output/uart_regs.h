#ifndef UART_REGS_H
#define UART_REGS_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

// Register offsets
#define UART_CTRL_OFFSET 0x0
#define UART_STATUS_OFFSET 0x4

// Register field masks and shifts
#define UART_CTRL_TX_EN_MASK 0x1
#define UART_CTRL_TX_EN_SHIFT 0
#define UART_CTRL_RX_EN_MASK 0x1
#define UART_CTRL_RX_EN_SHIFT 1
#define UART_STATUS_TX_FULL_MASK 0x1
#define UART_STATUS_TX_FULL_SHIFT 0
#define UART_STATUS_RX_EMPTY_MASK 0x1
#define UART_STATUS_RX_EMPTY_SHIFT 1

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
} uart_regs_t;

#ifdef __cplusplus
}
#endif

#endif  // UART_REGS_H