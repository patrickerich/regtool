from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path
import hjson
from regtool.parser.base import RegisterParser
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

class HjsonParser(RegisterParser):
    def parse(self):
        with open(self.input_file, 'r') as f:
            data = hjson.load(f)
            
        self.block_info = {
            'name': data['name'],
            'desc': data.get('desc', ''),
            'reg_aw': data.get('reg_aw', 8),
            'reg_dw': data.get('reg_dw', 32)
        }
        
        self.registers = data['registers']
        return self.block_info, self.registers

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
        return [self.parse_register(reg) for reg in self.registers]
