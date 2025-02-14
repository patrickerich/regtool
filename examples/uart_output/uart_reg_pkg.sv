package uart_reg_pkg;
  import uvm_pkg::*;
  `include "uvm_macros.svh"

  // Forward declarations
  class uart_reg_block extends uvm_reg_block;
    `uvm_object_utils(uart_reg_block)
    
    // CTRL Register
    rand ctrl_reg_c ctrl;
    // STATUS Register
    rand status_reg_c status;

    function new(string name = "uart_reg_block");
      super.new(name);
    endfunction

    virtual function void build();
      // Create default map
      default_map = create_map("default_map", 0, 32/8, UVM_LITTLE_ENDIAN);
      
      // Build CTRL
      ctrl = ctrl_reg_c::type_id::create("ctrl");
      ctrl.configure(this, null, "");
      ctrl.build();
      default_map.add_reg(ctrl, 'h0);
      // Build STATUS
      status = status_reg_c::type_id::create("status");
      status.configure(this, null, "");
      status.build();
      default_map.add_reg(status, 'h4);
    endfunction
  endclass

  // CTRL Register
  class ctrl_reg_c extends uvm_reg;
    `uvm_object_utils(ctrl_reg_c)
    
    // Fields
    rand uvm_reg_field tx_en;
    rand uvm_reg_field rx_en;

    function new(string name = "ctrl_reg_c");
      super.new(name, 32, UVM_NO_COVERAGE);
    endfunction

    virtual function void build();
      tx_en = uvm_reg_field::type_id::create("tx_en");
      tx_en.configure(this, 1, 0, "rw", 0, 32'h0, 1, 1, 1);
      rx_en = uvm_reg_field::type_id::create("rx_en");
      rx_en.configure(this, 1, 1, "rw", 0, 32'h0, 1, 1, 1);
    endfunction
  endclass

  // STATUS Register
  class status_reg_c extends uvm_reg;
    `uvm_object_utils(status_reg_c)
    
    // Fields
    rand uvm_reg_field tx_full;
    rand uvm_reg_field rx_empty;

    function new(string name = "status_reg_c");
      super.new(name, 32, UVM_NO_COVERAGE);
    endfunction

    virtual function void build();
      tx_full = uvm_reg_field::type_id::create("tx_full");
      tx_full.configure(this, 1, 0, "ro", 0, 32'h0, 1, 1, 1);
      rx_empty = uvm_reg_field::type_id::create("rx_empty");
      rx_empty.configure(this, 1, 1, "ro", 0, 32'h0, 1, 1, 1);
    endfunction
  endclass


endpackage