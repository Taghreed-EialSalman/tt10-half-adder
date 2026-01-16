# Half Adder – Tiny Tapeout Project

## How it works

This project implements a **Half Adder** digital circuit using Verilog.

A Half Adder adds two 1-bit binary inputs:

- **A**
- **B**

and produces two outputs:

- **SUM** = A ⊕ B (XOR)
- **CARRY** = A · B (AND)

### Truth Table

| A | B | SUM | CARRY |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

The design is implemented in `src/project.v` and follows combinational logic only (no clock, no memory).

---

## How to test

The project is tested using **cocotb** with **Icarus Verilog**.

### Local test steps

From the repository root:

```bash
cd test
make
