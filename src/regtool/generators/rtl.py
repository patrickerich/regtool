from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator

class RTLGenerator(RegisterGenerator):
    def generate(self):
        template_path = pkg_resources.files('regtool.templates.sv').joinpath('reg_block.sv.tpl')
        with template_path.open('r') as f:
            template_content = f.read()
            
        env = Environment(trim_blocks=True, lstrip_blocks=True)
        template = env.from_string(template_content)
        rtl = template.render(
            name=self.block_info['name'],
            registers=self.registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_reg_block.sv"
        output_file.write_text(rtl)
