from jinja2 import Environment
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator

class HeaderGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.c').joinpath('regs.h.tpl').open('r') as template_file:
            template_content = template_file.read()

        # Process registers to ensure correct data types
        processed_registers = []
        for register in self.registers:
            reg_copy = register.copy()
            if isinstance(reg_copy['reset_value'], str):
                reg_copy['reset_value'] = int(reg_copy['reset_value'], 16)
            for field in reg_copy['fields']:
                if isinstance(field['reset'], str):
                    field['reset'] = int(field['reset'], 16)
            processed_registers.append(reg_copy)

        env = Environment(trim_blocks=True, lstrip_blocks=True)
        template = env.from_string(template_content)
        header = template.render(
            name=self.block_info['name'],
            registers=processed_registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_regs.h"
        output_file.write_text(header)
