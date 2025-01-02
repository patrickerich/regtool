import pytest
from pathlib import Path
from regtool.generators.doc import generate_markdown, generate_html

def test_markdown_generation(tmp_path):
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
    generate_markdown(hjson_str, tmp_path)
    assert (tmp_path / "uart_registers.md").exists()

def test_html_generation(tmp_path):
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
    generate_html(hjson_str, tmp_path)
    assert (tmp_path / "uart_registers.html").exists()
