from pathlib import Path
from mako.template import Template
from regtool.parser.hjson_parser import HjsonParser
import importlib.resources as pkg_resources

def generate_rtl(reg_spec: str, output_dir: Path) -> None:
    parser = HjsonParser(reg_spec)
    registers = parser.get_registers()
    block_info = parser.get_block_info()

    # Use importlib.resources to access the template file
    with pkg_resources.files('regtool.templates.sv').joinpath('reg_block.sv.tpl').open('r') as template_file:
        template_content = template_file.read()

    template = Template(template_content)

    rtl = template.render(
        name=block_info['name'],
        registers=registers,
        regwidth=block_info['regwidth']
    )

    output_file = output_dir / f"{block_info['name']}_reg_block.sv"
    output_file.write_text(rtl)
