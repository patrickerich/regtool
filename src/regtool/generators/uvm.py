from pathlib import Path
from mako.template import Template
from regtool.parser.hjson_parser import HjsonParser

def generate_uvm(reg_spec: str, output_dir: Path) -> None:
    parser = HjsonParser(reg_spec)
    registers = parser.get_registers()
    block_info = parser.get_block_info()
    
    template_path = Path(__file__).parent.parent.parent.parent / 'templates' / 'uvm' / 'reg_pkg.sv.tpl'
    template = Template(filename=str(template_path))
    
    uvm = template.render(
        name=block_info['name'],
        registers=registers,
        regwidth=block_info['regwidth']
    )
    
    output_file = output_dir / f"{block_info['name']}_reg_pkg.sv"
    output_file.write_text(uvm)