package ${name}_reg_pkg;
  import uvm_pkg::*;
  `include "uvm_macros.svh"

  // Forward declarations
  class ${name}_reg_block extends uvm_reg_block;
    `uvm_object_utils(${name}_reg_block)
    
% for register in registers:
    // ${register.name} Register
    rand ${register.name.lower()}_reg_c ${register.name.lower()};
% endfor

    function new(string name = "${name}_reg_block");
      super.new(name);
    endfunction

    virtual function void build();
      default_map = create_map("default_map", 0, ${reg_dw}/8, UVM_LITTLE_ENDIAN);
      
% for register in registers:
      // Build ${register.name}
      ${register.name.lower()} = ${register.name.lower()}_reg_c::type_id::create("${register.name.lower()}");
      ${register.name.lower()}.configure(this, null, "");
      ${register.name.lower()}.build();
% if register.get('is_external', False):
      ${register.name.lower()}.set_external(1);
% endif
      default_map.add_reg(${register.name.lower()}, 'h${"%x" % register.offset});
% endfor
    endfunction
  endclass

% for register in registers:
  // ${register.name} Register
  class ${register.name.lower()}_reg_c extends uvm_reg;
    `uvm_object_utils(${register.name.lower()}_reg_c)
    
    // Fields
% for field in register.fields:
    rand uvm_reg_field ${field.name.lower()};
% endfor

    function new(string name = "${register.name.lower()}_reg_c");
      super.new(name, ${reg_dw}, UVM_NO_COVERAGE);
    endfunction

    virtual function void build();
% for field in register.fields:
      ${field.name.lower()} = uvm_reg_field::type_id::create("${field.name.lower()}");
      ${field.name.lower()}.configure(this, ${field.width}, ${field.lsb}, "${register.swaccess}", 0, ${reg_dw}'h${"%x" % (field.reset if field.reset is not None else 0)}, 1, 1, 1);
% endfor
    endfunction
  endclass

% endfor

endpackage