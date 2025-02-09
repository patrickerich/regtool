from pathlib import Path
from regtool.parser.hjson_parser import HjsonParser

class RegisterGenerator:
    def __init__(self, block_info, registers, output_dir):
        self.block_info = block_info
        self.registers = registers
        self.output_dir = output_dir

    def generate(self):
        raise NotImplementedError("Subclasses must implement generate()")
