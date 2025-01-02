import pytest
from regtool.parser.reg_model import RegisterModel, BitField

def test_bitfield_width():
    field = BitField(name="TEST", msb=7, lsb=0, desc="Test field")
    assert field.width == 8
    assert field.mask == 0xFF

def test_register_validation():
    fields = [
        BitField(name="F1", msb=7, lsb=4, desc="Field 1"),
        BitField(name="F2", msb=3, lsb=0, desc="Field 2")
    ]
    reg = RegisterModel(
        name="TEST",
        offset=0x0,
        desc="Test register",
        fields=fields,
        swaccess="rw",
        hwaccess="hro"
    )
    reg.validate()  # Should not raise exception
