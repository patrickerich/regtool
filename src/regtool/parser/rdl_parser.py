from systemrdl import RDLCompiler, RDLListener, RDLWalker, WalkerAction
from systemrdl.node import Node
from regtool.parser.base import RegisterParser

class RDLParser(RegisterParser):
    def parse(self):
        rdlc = RDLCompiler()
        rdlc.compile_file(self.input_file)
        root = rdlc.elaborate()
        
        # Extract register block info
        top_node = root.top
        self.block_info = {
            'name': top_node.inst_name,
            'desc': top_node.get_property('desc') or '',
            'reg_aw': 32,
            'reg_dw': 32
        }
        
        # Walk register nodes and build register list
        walker = RDLWalker()
        listener = RegisterExtractor()
        walker.walk(top_node, listener)
        self.registers = listener.registers

        return self.block_info, self.registers

class RegisterExtractor(RDLListener):
    def __init__(self):
        super().__init__()
        self.registers = []

    def enter_Reg(self, node):
        register = {
            'name': node.inst_name,
            'desc': node.get_property('desc') or '',
            'offset': node.absolute_address,
            'swaccess': 'rw',  # Default access mode
            'fields': []
        }
        
        for field in node.fields():
            register['fields'].append({
                'name': field.inst_name,
                'desc': field.get_property('desc') or '',
                'lsb': field.lsb,
                'msb': field.msb,
                'width': field.msb - field.lsb + 1,
                'reset': 0  # Default reset value
            })
            
        self.registers.append(register)
        return WalkerAction.Continue
