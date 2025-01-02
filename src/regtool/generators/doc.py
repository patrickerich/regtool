from pathlib import Path
from mako.template import Template
from regtool.parser.hjson_parser import HjsonParser
import importlib.resources as pkg_resources

def generate_markdown(reg_spec: str, output_dir: Path) -> None:
    parser = HjsonParser(reg_spec)
    registers = parser.get_registers()
    block_info = parser.get_block_info()

    with pkg_resources.files('regtool.templates.doc').joinpath('registers.md.tpl').open('r') as template_file:
        template_content = template_file.read()

    template = Template(template_content)

    md = template.render(
        name=block_info['name'],
        desc=block_info['desc'],
        registers=registers
    )

    output_file = output_dir / f"{block_info['name']}_registers.md"
    output_file.write_text(md)

def generate_html(reg_spec: str, output_dir: Path) -> None:
    parser = HjsonParser(reg_spec)
    registers = parser.get_registers()
    block_info = parser.get_block_info()

    with pkg_resources.files('regtool.templates.doc').joinpath('registers.html.tpl').open('r') as template_file:
        template_content = template_file.read()

    template = Template(template_content)

    html = template.render(
        name=block_info['name'],
        desc=block_info['desc'],
        registers=registers
    )

    output_file = output_dir / f"{block_info['name']}_registers.html"
    output_file.write_text(html)
