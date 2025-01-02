import pytest
from pathlib import Path
from regtool.generators.rtl import generate_rtl

def test_rtl_generation(tmp_path):
    hjson_str = """
    {
        name: "uart",
        registers: [
            {
                name: "CTRL",
                desc: "Control Register",
                swaccess: "rw",
                offset: "0x00",
                fields: [
                    {
                        bits: "0",
                        name: "TX_EN",
                        desc: "Transmitter Enable"
                    }
                ]
            }
        ]
    }
    """
    generate_rtl(hjson_str, tmp_path)
    assert (tmp_path / "uart_reg_block.sv").exists()
