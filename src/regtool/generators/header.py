from jinja2 import Environment, FileSystemLoader
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator

class HeaderGenerator(RegisterGenerator):
    def generate(self):
        template_path = pkg_resources.files('regtool.templates.c').joinpath('regs.h.tpl')
        with template_path.open('r') as f:
            template_content = f.read()
            
        def mask_value(width):
            return f"0x{((1 << width) - 1):x}"
            
        env = Environment(trim_blocks=True, lstrip_blocks=True)
        env.filters['mask_value'] = mask_value
        template = env.from_string(template_content)
        header = template.render(
            name=self.block_info['name'],
            registers=self.registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_regs.h"
        output_file.write_text(header)
