from pathlib import Path
from jinja2 import Environment
import importlib.resources as pkg_resources
from regtool.parser.hjson_parser import HjsonParser
from regtool.generators.base import RegisterGenerator

class MarkdownGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.doc').joinpath('registers.md.tpl').open('r') as template_file:
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
        md = template.render(
            name=self.block_info['name'],
            desc=self.block_info['desc'],
            registers=processed_registers
        )

        output_file = self.output_dir / f"{self.block_info['name']}_registers.md"
        output_file.write_text(md)

class HTMLGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.doc').joinpath('registers.html.tpl').open('r') as template_file:
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
        html = template.render(
            name=self.block_info['name'],
            desc=self.block_info['desc'],
            registers=processed_registers
        )

        output_file = self.output_dir / f"{self.block_info['name']}_registers.html"
        output_file.write_text(html)