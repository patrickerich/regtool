#!/usr/bin/env python3
import argparse
from pathlib import Path
from regtool.generators.rtl import RTLGenerator
from regtool.generators.doc import MarkdownGenerator, HTMLGenerator
from regtool.generators.uvm import UVMGenerator
from regtool.generators.header import HeaderGenerator

def main():
                   parser = argparse.ArgumentParser(
                       description="Register generation tool"
                   )
    
                   parser.add_argument('input',
                                       type=argparse.FileType('r'),
                                       help='Input register definition file (HJSON)')
                       
                   parser.add_argument('--rtl',
                                       action='store_true',
                                       help='Generate SystemVerilog RTL')
                       
                   parser.add_argument('--doc',
                                       action='store_true',
                                       help='Generate Markdown documentation')
                       
                   parser.add_argument('--html',
                                       action='store_true',
                                       help='Generate HTML documentation')
                       
                   parser.add_argument('--uvm',
                                       action='store_true', 
                                       help='Generate UVM register model')
                       
                   parser.add_argument('--cheader',
                                       action='store_true',
                                       help='Generate C header file')
                       
                   parser.add_argument('--outdir',
                                       type=Path,
                                       help='Output directory')

                   args = parser.parse_args()
    
                   if args.outdir:
                       args.outdir.mkdir(parents=True, exist_ok=True)
        
                   reg_spec = args.input.read()
    
                   if args.rtl:
                       rtl_generator = RTLGenerator(reg_spec, args.outdir)
                       rtl_generator.generate()
        
                   if args.doc:
                       markdown_generator = MarkdownGenerator(reg_spec, args.outdir)
                       markdown_generator.generate()
        
                   if args.html:
                       html_generator = HTMLGenerator(reg_spec, args.outdir)
                       html_generator.generate()
        
                   if args.uvm:
                       uvm_generator = UVMGenerator(reg_spec, args.outdir)
                       uvm_generator.generate()
        
                   if args.cheader:
                       header_generator = HeaderGenerator(reg_spec, args.outdir)
                       header_generator.generate()

if __name__ == '__main__':
                   main()
