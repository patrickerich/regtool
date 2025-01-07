from pathlib import Path
from mako.template import Template
import importlib.resources as pkg_resources
from regtool.parser.hjson_parser import HjsonParser
from regtool.generators.base import RegisterGenerator

class MarkdownGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.doc').joinpath('registers.md.tpl').open('r') as template_file:
            template_content = template_file.read()

        template = Template(template_content)
        md = template.render(
            name=self.block_info['name'],
            desc=self.block_info['desc'],
            registers=self.registers
        )

        output_file = self.output_dir / f"{self.block_info['name']}_registers.md"
        output_file.write_text(md)

class HTMLGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.doc').joinpath('registers.html.tpl').open('r') as template_file:
            template_content = template_file.read()

        template = Template(template_content)
        html = template.render(
            name=self.block_info['name'],
            desc=self.block_info['desc'],
            registers=self.registers
        )

        output_file = self.output_dir / f"{self.block_info['name']}_registers.html"
        output_file.write_text(html)
