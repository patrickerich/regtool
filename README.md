# Register Tool (regtool)

This repo implements a hardware register generation tool written in Python.
Eventually, this tool should support everything supported by PeakRDL (and more).

A key consideration for the RTL generated with this register tool is (or rather will be) that the resulting hardware is optimized for power. Details are still TBD.

## Features
A register generation tool for hardware designs that generates:
- SystemVerilog RTL
- UVM register models
- C headers
- Documentation (Markdown/HTML)

The following components are independently implemented:
- Parsers (HJSON and RDL)
- Generators (RTL, UVM, Markdown, HTML, C header)
- Templates

This should facilitate easy future improvements and additions.

## Installation
To install the tool, use the following command:
```bash
pip install git+https://github.com/patrickerich/regtool.git
```

## Status
This project is in an early stage of development. It is very likely that it does not work properly yet!

### In progress
The features that are currently being implemented/added:
1. RDL input
2. Register array support
3. Register access types (partial)
4. Memory regions
5. External registers (partial)
6. Register aliases
7. Register reset values

### Features Under Construction
The following features are temporarily disabled while we improve their implementation:
1. Register arrays
2. Register aliases
3. HTML documentation navigation
4. Advanced HTML styling
5. Advanced register access types
6. Memory regions
7. Full external register support

## Usage
To see the available options and usage information, run:
```bash
regtool --help
```

## Example
Here is an example of how to use the tool:
```bash
regtool input_file.hjson --outdir output_directory --rtl --uvm --cheader --doc --html
```
- `input_file.hjson`: Specifies the input file.
- `--outdir`: Specifies the output directory.
- `--rtl`: Generate SystemVerilog RTL.
- `--uvm`: Generate UVM register model.
- `--cheader`: Generate C header.
- `--doc`: Generate markdown documentation.
- `--html`: Generate HTML documentation.

<!--
## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
-->

## License
This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.
