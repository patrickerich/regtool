# UART Register Documentation

UART peripheral registers

## Register Map

| Offset | Name | Description | Reset Value | Type | Access | HW Access | Aliases |
|--------|------|-------------|-------------|------|---------|-----------|----------|
| 0x0 | ctrl | Control Register | 0x0 | Internal | rw | none | - |
| 0x4 | status | Status Register | 0x0 | Internal | rw | none | - |
| 0x8 | data | Data Register | 0x0 | Internal | rw | none | - |
## Register Details

### ctrl (0x0)
Control Register

Type: Internal
Reset Value: 0x0
Software Access: rw
Hardware Access: none

| Bits | Name | Access | Reset | HW Access | Description |
|------|------|--------|--------|------------|-------------|
| 0 | en | rw | 0x0 | none | UART Enable |
| 1 | parity | rw | 0x0 | none | Parity Enable |
### status (0x4)
Status Register

Type: Internal
Reset Value: 0x0
Software Access: rw
Hardware Access: none

| Bits | Name | Access | Reset | HW Access | Description |
|------|------|--------|--------|------------|-------------|
| 0 | txfull | rw | 0x0 | none | Transmit FIFO Full |
| 1 | rxempty | rw | 0x0 | none | Receive FIFO Empty |
### data (0x8)
Data Register

Type: Internal
Reset Value: 0x0
Software Access: rw
Hardware Access: none

| Bits | Name | Access | Reset | HW Access | Description |
|------|------|--------|--------|------------|-------------|
| 7:0 | value | rw | 0x0 | none | Data Value |
