from pathlib import Path
from jinja2 import Environment
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator

class UVMGenerator(RegisterGenerator):
    def generate(self):
        template_path = pkg_resources.files('regtool.templates.uvm').joinpath('reg_pkg.sv.tpl')
        with template_path.open('r') as f:
            template_content = f.read()
            
        env = Environment(trim_blocks=True, lstrip_blocks=True)
        template = env.from_string(template_content)
        uvm = template.render(
            name=self.block_info['name'],
            registers=self.registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_reg_pkg.sv"
        output_file.write_text(uvm)
