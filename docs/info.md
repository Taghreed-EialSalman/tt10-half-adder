# Half Adder

## How it works
This design implements a 1-bit **Half Adder**.

Inputs:
- `ui_in[0]` = A
- `ui_in[1]` = B

Outputs:
- `uo_out[0]` = SUM = A ^ B
- `uo_out[1]` = CARRY = A & B
- `uo_out[7:2]` are tied to 0

The bidirectional IOs are unused:
- `uio_out` = 0
- `uio_oe`  = 0

## How to test
The module is verified using cocotb.

From the repository root:
```bash
cd test
make
