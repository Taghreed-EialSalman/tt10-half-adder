# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_half_adder(dut):
    dut._log.info("Starting Half Adder Test")

    # Clock (required by template)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Test all input combinations
    test_vectors = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    ]

    for a, b in test_vectors:
        # Put A and B on ui_in[0] and ui_in[1]
        dut.ui_in.value = (b << 1) | a
        await ClockCycles(dut.clk, 1)

        sum_out = dut.uo_out.value.integer & 0x1
        carry_out = (dut.uo_out.value.integer >> 1) & 0x1

        expected_sum = a ^ b
        expected_carry = a & b

        dut._log.info(
            f"A={a}, B={b} -> SUM={sum_out}, CARRY={carry_out}"
        )

        assert sum_out == expected_sum, f"SUM mismatch for A={a}, B={b}"
        assert carry_out == expected_carry, f"CARRY mismatch for A={a}, B={b}"

    dut._log.info("Half Adder test PASSED ✅")
