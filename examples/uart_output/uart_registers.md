# UART Register Documentation

Universal Asynchronous Receiver/Transmitter


| Offset | Name | Description |
|--------|------|-------------|
| 0x0 | CTRL | Control Register |
| 0x4 | STATUS | Status Register |


Control Register

| Bits | Name | Access | Description |
|------|------|--------|-------------|
| 0 | TX_EN | rw | Transmitter Enable |
| 1 | RX_EN | rw | Receiver Enable |

Status Register

| Bits | Name | Access | Description |
|------|------|--------|-------------|
| 0 | TX_FULL | ro | TX FIFO Full |
| 1 | RX_EMPTY | ro | RX FIFO Empty |

