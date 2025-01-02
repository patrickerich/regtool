#!/usr/bin/env python3
import argparse
from pathlib import Path
from regtool.generators.rtl import generate_rtl
from regtool.generators.doc import generate_markdown, generate_html
from regtool.generators.uvm import generate_uvm
from regtool.generators.header import generate_header

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
        generate_rtl(reg_spec, args.outdir)
        
    if args.doc:
        generate_markdown(reg_spec, args.outdir)
        
    if args.html:
        generate_html(reg_spec, args.outdir)
        
    if args.uvm:
        generate_uvm(reg_spec, args.outdir)
        
    if args.cheader:
        generate_header(reg_spec, args.outdir)

if __name__ == '__main__':
    main()
