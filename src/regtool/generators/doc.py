from pathlib import Path
from mako.template import Template
from regtool.parser.hjson_parser import HjsonParser

def generate_markdown(reg_spec: str, output_dir: Path) -> None:
    parser = HjsonParser(reg_spec)
    registers = parser.get_registers()
    block_info = parser.get_block_info()
    
    template_path = Path(__file__).parent.parent.parent.parent / 'templates' / 'doc' / 'registers.md.tpl'
    template = Template(filename=str(template_path))
    
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
    
    template_path = Path(__file__).parent.parent.parent.parent / 'templates' / 'doc' / 'registers.html.tpl'
    template = Template(filename=str(template_path))
    
    html = template.render(
        name=block_info['name'],
        desc=block_info['desc'],
        registers=registers
    )
    
    output_file = output_dir / f"{block_info['name']}_registers.html"
    output_file.write_text(html)
