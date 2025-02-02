from pathlib import Path
from jinja2 import Environment
import importlib.resources as pkg_resources
from regtool.parser.hjson_parser import HjsonParser
from regtool.generators.base import RegisterGenerator

class MarkdownGenerator(RegisterGenerator):
    def generate(self):
        template_path = pkg_resources.files('regtool.templates.doc').joinpath('registers.md.tpl')
        with template_path.open('r') as f:
            template_content = f.read()
            
        env = Environment(trim_blocks=True, lstrip_blocks=True)
        template = env.from_string(template_content)
        md = template.render(
            name=self.block_info['name'],
            desc=self.block_info['desc'],
            registers=self.registers
        )

        output_file = self.output_dir / f"{self.block_info['name']}_registers.md"
        output_file.write_text(md)

class HTMLGenerator(RegisterGenerator):
    def generate(self):
        template_path = pkg_resources.files('regtool.templates.doc').joinpath('registers.html.tpl')
        with template_path.open('r') as f:
            template_content = f.read()
            
        env = Environment(trim_blocks=True, lstrip_blocks=True)
        template = env.from_string(template_content)
        html = template.render(
            name=self.block_info['name'],
            desc=self.block_info['desc'],
            registers=self.registers
        )

        output_file = self.output_dir / f"{self.block_info['name']}_registers.html"
        output_file.write_text(html)