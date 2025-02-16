from pathlib import Path
from jinja2 import Environment
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator
from regtool.parser.reg_model import RegisterModel, BitField

class MarkdownGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.doc').joinpath('registers.md.tpl').open('r') as template_file:
            template_content = template_file.read()
        env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            variable_start_string='${',
            variable_end_string='}',
            keep_trailing_newline=True,
            line_statement_prefix='%'
        )
        env.globals['str'] = str

        # Convert to RegisterModel instances
        processed_registers = []
        for reg in self.registers:
            fields = [BitField(
                name=f['name'],
                msb=f['msb'],
                lsb=f['lsb'],
                desc=f['desc'],
                reset=int(f.get('reset', '0'), 16) if isinstance(f.get('reset'), str) else f.get('reset', 0)
            ) for f in reg['fields']]
            
            register = RegisterModel(
                name=reg['name'],
                offset=int(reg['offset'], 16) if isinstance(reg['offset'], str) else reg['offset'],
                desc=reg['desc'],
                fields=fields,
                swaccess=reg.get('swaccess', 'rw'),
                hwaccess=reg.get('hwaccess', 'none'),
                reset_value=int(reg.get('reset_value', '0'), 16) if isinstance(reg.get('reset_value'), str) else reg.get('reset_value', 0),
                aliases=reg['aliases']() if callable(reg.get('aliases')) else reg.get('aliases', []),
                is_external=reg.get('is_external', False),
                is_array=reg.get('is_array', False),
                array_size=reg.get('array_size', 0),
                array_stride=reg.get('array_stride', 0)
            )
            processed_registers.append(register)

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

        env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            variable_start_string='${',
            variable_end_string='}',
            keep_trailing_newline=True,
            line_statement_prefix='%'
        )
        env.globals['str'] = str

        # Convert to RegisterModel instances
        processed_registers = []
        for reg in self.registers:
            fields = [BitField(
                name=f['name'],
                msb=f['msb'],
                lsb=f['lsb'],
                desc=f['desc'],
                reset=int(f.get('reset', '0'), 16) if isinstance(f.get('reset'), str) else f.get('reset', 0)
            ) for f in reg['fields']]
            
            register = RegisterModel(
                name=reg['name'],
                offset=int(reg['offset'], 16) if isinstance(reg['offset'], str) else reg['offset'],
                desc=reg['desc'],
                fields=fields,
                swaccess=reg.get('swaccess', 'rw'),
                hwaccess=reg.get('hwaccess', 'none'),
                reset_value=int(reg.get('reset_value', '0'), 16) if isinstance(reg.get('reset_value'), str) else reg.get('reset_value', 0),
                aliases=reg['aliases']() if callable(reg.get('aliases')) else reg.get('aliases', []),
                is_external=reg.get('is_external', False),
                is_array=reg.get('is_array', False),
                array_size=reg.get('array_size', 0),
                array_stride=reg.get('array_stride', 0)
            )
            processed_registers.append(register)

        template = env.from_string(template_content)
        html = template.render(
            name=self.block_info['name'],
            desc=self.block_info['desc'],
            registers=processed_registers
        )

        output_file = self.output_dir / f"{self.block_info['name']}_registers.html"
        output_file.write_text(html)
        