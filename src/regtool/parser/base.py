class RegisterParser:
    def __init__(self, input_file):
        self.input_file = input_file
        self.block_info = {}
        self.registers = []

    def parse(self):
        """Parse register description and return block info and registers.
        
        Returns:
            tuple: (block_info, registers)
        """
        raise NotImplementedError("Subclasses must implement parse()")
