import pytest
from pathlib import Path
from regtool.generators.header import generate_header

def test_header_generation(tmp_path):
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
    generate_header(hjson_str, tmp_path)
    assert (tmp_path / "uart_regs.h").exists()
