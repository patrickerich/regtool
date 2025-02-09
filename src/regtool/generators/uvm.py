from pathlib import Path
from jinja2 import Environment
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator

class UVMGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.uvm').joinpath('reg_pkg.sv.tpl').open('r') as template_file:
            template_content = template_file.read()

        # Process registers to ensure correct data types
        processed_registers = []
        for register in self.registers:
            reg_copy = register.copy()
            # Convert offset to integer
            if isinstance(reg_copy['offset'], str):
                reg_copy['offset'] = int(reg_copy['offset'], 16)
            
            # Process reset values
            if isinstance(reg_copy['reset_value'], str):
                reg_copy['reset_value'] = int(reg_copy['reset_value'], 16)
            
            # Process field reset values
            for field in reg_copy['fields']:
                if isinstance(field['reset'], str):
                    field['reset'] = int(field['reset'], 16)
                
            processed_registers.append(reg_copy)

        env = Environment(trim_blocks=True, lstrip_blocks=True)
        template = env.from_string(template_content)
        uvm = template.render(
            name=self.block_info['name'],
            registers=processed_registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_reg_pkg.sv"
        output_file.write_text(uvm)