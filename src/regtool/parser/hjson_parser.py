from pathlib import Path
import hjson
from regtool.parser.base import RegisterParser

class HjsonParser(RegisterParser):
    def parse(self):
        with open(self.input_file, 'r') as f:
            data = hjson.load(f)
            
        self.block_info = {
            'name': data['name'],
            'desc': data.get('desc', ''),
            'reg_aw': data.get('reg_aw', 32),
            'reg_dw': data.get('reg_dw', 32)
        }
        
        self.registers = []
        for reg in data['registers']:
            register = {
                'name': reg['name'],
                'desc': reg.get('desc', ''),
                'offset': reg['offset'],
                'aliases': reg.get('aliases', []),
                'swaccess': reg.get('swaccess', 'rw'),
                'hwaccess': reg.get('hwaccess', 'none'),
                'is_array': reg.get('is_array', False),
                'array_size': reg.get('array_size', 1),
                'array_stride': reg.get('array_stride', 4),
                'is_external': reg.get('external', False),
                'reset_value': reg.get('reset', 0),
                'fields': []
            }
            
            for field in reg['fields']:
                if 'bits' in field:
                    bits = field['bits'].split(':')
                    msb = int(bits[0])
                    lsb = int(bits[1]) if len(bits) > 1 else msb
                else:
                    msb = field.get('msb', field.get('bit', 0))
                    lsb = field.get('lsb', field.get('bit', 0))

                register['fields'].append({
                    'name': field['name'],
                    'desc': field.get('desc', ''),
                    'lsb': lsb,
                    'msb': msb,
                    'width': msb - lsb + 1,
                    'reset': field.get('reset', 0),
                    'resetsignal': field.get('resetsignal', 'rst_ni')
                })
                
            self.registers.append(register)
            
        return self.block_info, self.registers