#!/usr/bin/env python3
from pathlib import Path
import argparse
import sys
from regtool.parser.hjson_parser import HjsonParser
from regtool.parser.rdl_parser import RDLParser
from regtool.generators.rtl import RTLGenerator
from regtool.generators.uvm import UVMGenerator
from regtool.generators.header import HeaderGenerator
from regtool.generators.doc import MarkdownGenerator, HTMLGenerator

def main():
    parser = argparse.ArgumentParser(
        description='Register generation tool for hardware designs'
    )
    parser.add_argument('input', help='Input register description file (HJSON or RDL)')
    parser.add_argument('--outdir', default='.', help='Output directory')
    parser.add_argument('--rtl', action='store_true', help='Generate SystemVerilog RTL')
    parser.add_argument('--uvm', action='store_true', help='Generate UVM register model')
    parser.add_argument('--cheader', action='store_true', help='Generate C header')
    parser.add_argument('--doc', action='store_true', help='Generate markdown documentation')
    parser.add_argument('--html', action='store_true', help='Generate HTML documentation')

    args = parser.parse_args()

    input_file = Path(args.input)
    output_dir = Path(args.outdir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Select parser based on file extension
    if input_file.suffix == '.rdl':
        reg_parser = RDLParser(input_file)
    else:
        reg_parser = HjsonParser(input_file)

    block_info, registers = reg_parser.parse()

    if args.rtl:
        rtl_generator = RTLGenerator(block_info, registers, output_dir)
        rtl_generator.generate()

    if args.uvm:
        uvm_generator = UVMGenerator(block_info, registers, output_dir)
        uvm_generator.generate()

    if args.cheader:
        header_generator = HeaderGenerator(block_info, registers, output_dir)
        header_generator.generate()

    if args.doc:
        md_generator = MarkdownGenerator(block_info, registers, output_dir)
        md_generator.generate()

    if args.html:
        html_generator = HTMLGenerator(block_info, registers, output_dir)
        html_generator.generate()

    return 0

if __name__ == '__main__':
    sys.exit(main())
