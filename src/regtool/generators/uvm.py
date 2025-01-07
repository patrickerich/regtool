from pathlib import Path
from mako.template import Template
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator

class UVMGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.uvm').joinpath('reg_pkg.sv.tpl').open('r') as template_file:
            template_content = template_file.read()

        template = Template(template_content)
        uvm = template.render(
            name=self.block_info['name'],
            registers=self.registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_reg_pkg.sv"
        output_file.write_text(uvm)
