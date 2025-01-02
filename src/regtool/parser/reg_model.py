
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BitField:
    """Register bit field model"""
    name: str
    msb: int  
    lsb: int
    desc: str
    reset: Optional[int] = None
    
    @property
    def width(self) -> int:
        """Get field width in bits"""
        return self.msb - self.lsb + 1
        
    @property 
    def mask(self) -> int:
        """Get field mask"""
        return ((1 << self.width) - 1) << self.lsb

@dataclass
class RegisterModel:
    """Register model"""
    name: str
    offset: int
    desc: str
    fields: List[BitField]
    swaccess: str  
    hwaccess: str
    
    def get_field_by_name(self, name: str) -> Optional[BitField]:
        """Get field by name"""
        for field in self.fields:
            if field.name == name:
                return field
        return None
        
    @property
    def width(self) -> int:
        """Get total register width"""
        return max(f.msb for f in self.fields) + 1
        
    def validate(self) -> None:
        """Validate register model"""
        # Check for overlapping fields
        bits_used = set()
        for field in self.fields:
            field_bits = set(range(field.lsb, field.msb + 1))
            if field_bits & bits_used:
                raise ValueError(f"Overlapping fields in register {self.name}")
            bits_used.update(field_bits)
