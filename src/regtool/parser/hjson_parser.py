
from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path
import hjson
from .reg_model import RegisterModel, BitField

@dataclass
class RegisterSpec:
    """Register specification from HJSON"""
    name: str
    desc: str
    offset: str
    swaccess: str
    hwaccess: str
    fields: List[Dict]

class HjsonParser:
    def __init__(self, hjson_str: str):
        self.raw_spec = hjson.loads(hjson_str)
        self.validate()
        
    def validate(self) -> None:
        """Validate required fields in register specification"""
        required = ['name', 'registers']
        for field in required:
            if field not in self.raw_spec:
                raise ValueError(f"Missing required field: {field}")
                
        for reg in self.raw_spec['registers']:
            if not all(k in reg for k in ['name', 'fields']):
                raise ValueError(f"Invalid register specification: {reg}")
    
    def parse_register(self, reg_dict: Dict) -> RegisterModel:
        """Parse single register definition into RegisterModel"""
        fields = []
        for field in reg_dict['fields']:
            if ':' in field['bits']:
                msb, lsb = map(int, field['bits'].split(':'))
            else:
                msb = lsb = int(field['bits'])
            
            fields.append(BitField(
                name=field['name'],
                msb=msb,
                lsb=lsb,
                desc=field.get('desc', ''),
                reset=field.get('reset')
            ))
            
        return RegisterModel(
            name=reg_dict['name'],
            offset=int(reg_dict['offset'], 16),
            desc=reg_dict.get('desc', ''),
            fields=fields,
            swaccess=reg_dict.get('swaccess', 'rw'),
            hwaccess=reg_dict.get('hwaccess', 'hro')
        )
        
    def get_registers(self) -> List[RegisterModel]:
        """Get list of all registers"""
        return [self.parse_register(reg) for reg in self.raw_spec['registers']]
        
    def get_block_info(self) -> Dict:
        """Get block-level information"""
        return {
            'name': self.raw_spec['name'],
            'version': self.raw_spec.get('version', '1.0.0'),
            'regwidth': self.raw_spec.get('regwidth', 32),
            'desc': self.raw_spec.get('one_line_desc', '')
        }
