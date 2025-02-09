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
                'swaccess': reg.get('swaccess', 'rw'),
                'is_array': reg.get('is_array', False),
                'array_size': reg.get('array_size', 1),
                'array_stride': reg.get('array_stride', 4),
                'is_external': reg.get('external', False),
                'fields': []
            }
            
            for field in reg['fields']:
                register['fields'].append({
                    'name': field['name'],
                    'desc': field.get('desc', ''),
                    'lsb': field['lsb'],
                    'msb': field['msb'],
                    'width': field['msb'] - field['lsb'] + 1,
                    'reset': field.get('reset', 0)
                })
                
            self.registers.append(register)
            
        self.memories = []
        for mem in data.get('memories', []):
            memory = {
                'name': mem['name'],
                'desc': mem.get('desc', ''),
                'offset': mem['offset'],
                'size': mem['size'],
                'width': mem['width'],
                'type': 'mem'
            }
            self.memories.append(memory)
            
        return self.block_info, self.registers