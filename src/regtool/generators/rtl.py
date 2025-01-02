
from pathlib import Path
from mako.template import Template
from regtool.parser.hjson_parser import HjsonParser

def generate_rtl(reg_spec: str, output_dir: Path) -> None:
    parser = HjsonParser(reg_spec)
    registers = parser.get_registers()
    block_info = parser.get_block_info()
    
    template_path = Path(__file__).parent.parent.parent.parent / 'templates' / 'sv' / 'reg_block.sv.tpl'
    template = Template(filename=str(template_path))
    
    rtl = template.render(
        name=block_info['name'],
        registers=registers,
        regwidth=block_info['regwidth']
    )
    
    output_file = output_dir / f"{block_info['name']}_reg_block.sv"
    output_file.write_text(rtl)
