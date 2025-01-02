import pytest
from regtool.parser.hjson_parser import HjsonParser

def test_parse_valid_register():
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
    parser = HjsonParser(hjson_str)
    registers = parser.get_registers()
    assert len(registers) == 1
    assert registers[0].name == "CTRL"
    assert registers[0].fields[0].name == "TX_EN"
