from pathlib import Path
from jinja2 import Environment
import importlib.resources as pkg_resources
from regtool.generators.base import RegisterGenerator
from regtool.parser.reg_model import RegisterModel, BitField

class HeaderGenerator(RegisterGenerator):
    def generate(self):
        with pkg_resources.files('regtool.templates.c').joinpath('regs.h.tpl').open('r') as template_file:
            template_content = template_file.read()
        env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            variable_start_string='${',
            variable_end_string='}',
            keep_trailing_newline=True,
            line_statement_prefix='%'
        )
        env.globals['enumerate'] = enumerate
        
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
                offset=reg['offset'],
                desc=reg['desc'],
                fields=fields,
                swaccess=reg.get('swaccess', 'rw'),
                hwaccess=reg.get('hwaccess', 'none'),
                reset_value=int(reg.get('reset_value', '0'), 16) if isinstance(reg.get('reset_value'), str) else reg.get('reset_value', 0)
            )
            processed_registers.append(register)

        template = env.from_string(template_content)
        header = template.render(
            name=self.block_info['name'],
            registers=processed_registers,
            reg_aw=self.block_info['reg_aw'],
            reg_dw=self.block_info['reg_dw']
        )

        output_file = self.output_dir / f"{self.block_info['name']}_regs.h"
        output_file.write_text(header)
