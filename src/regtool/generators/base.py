from pathlib import Path
from regtool.parser.hjson_parser import HjsonParser

class RegisterGenerator:
    def __init__(self, reg_spec: str, output_dir: Path):
        self.reg_spec = reg_spec
        self.output_dir = output_dir
        self.parser = HjsonParser(reg_spec)
        self.registers = self.parser.get_registers()
        self.block_info = self.parser.get_block_info()

    def generate(self):
        raise NotImplementedError("Subclasses should implement this method.")
