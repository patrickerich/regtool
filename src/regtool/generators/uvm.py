from pathlib import Path
from mako.template import Template
from regtool.parser.hjson_parser import HjsonParser
import importlib.resources as pkg_resources

def generate_uvm(reg_spec: str, output_dir: Path) -> None:
    parser = HjsonParser(reg_spec)
    registers = parser.get_registers()
    block_info = parser.get_block_info()

    with pkg_resources.files('regtool.templates.uvm').joinpath('reg_pkg.sv.tpl').open('r') as template_file:
        template_content = template_file.read()

    template = Template(template_content)

    uvm = template.render(
        name=block_info['name'],
        registers=registers,
        regwidth=block_info['regwidth']
    )

    output_file = output_dir / f"{block_info['name']}_reg_pkg.sv"
    output_file.write_text(uvm)
