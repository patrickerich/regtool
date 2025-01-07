from mako.template import Template
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator

class HeaderGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.c').joinpath('regs.h.tpl').open('r') as template_file:
            template_content = template_file.read()

        template = Template(template_content)
        header = template.render(
            name=self.block_info['name'],
            registers=self.registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_regs.h"
        output_file.write_text(header)
