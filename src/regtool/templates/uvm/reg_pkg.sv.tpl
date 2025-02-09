package ${name}_reg_pkg;
  import uvm_pkg::*;
  `include "uvm_macros.svh"

  // Forward declarations
  class ${name}_reg_block extends uvm_reg_block;
    `uvm_object_utils(${name}_reg_block)
    
% for register in registers:
    // ${register.name} Register
% if register.is_array:
    rand ${register.name.lower()}_reg_c ${register.name.lower()}[${register.array_size}];
% else:
    rand ${register.name.lower()}_reg_c ${register.name.lower()};
% endif
% endfor

    function new(string name = "${name}_reg_block");
      super.new(name);
    endfunction

    virtual function void build();
      // Create default map
      default_map = create_map("default_map", 0, ${reg_dw}/8, UVM_LITTLE_ENDIAN);
      
% for register in registers:
      // Build ${register.name}
% if register.is_array:
      foreach(${register.name.lower()}[i]) begin
        ${register.name.lower()}[i] = ${register.name.lower()}_reg_c::type_id::create($sformatf("${register.name.lower()}_%0d", i));
        ${register.name.lower()}[i].configure(this, null, "");
        ${register.name.lower()}[i].build();
        default_map.add_reg(${register.name.lower()}[i], 'h${"%x" % register.offset} + i * 'h${"%x" % register.array_stride});
      end
% else:
      ${register.name.lower()} = ${register.name.lower()}_reg_c::type_id::create("${register.name.lower()}");
      ${register.name.lower()}.configure(this, null, "");
      ${register.name.lower()}.build();
      default_map.add_reg(${register.name.lower()}, 'h${"%x" % register.offset});
% for alias in register.get('aliases', []):
      default_map.add_reg(${register.name.lower()}, 'h${"%x" % alias});  // Alias
% endfor
% endif
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
      super.new(name, ${reg_dw}, ${register.is_external ? "UVM_NO_COVERAGE" : "UVM_FULL_COVERAGE"});
    endfunction

    virtual function void build();
% for field in register.fields:
      ${field.name.lower()} = uvm_reg_field::type_id::create("${field.name.lower()}");
      ${field.name.lower()}.configure(this, ${field.width}, ${field.lsb}, 
                                    "${register.swaccess}", 
                                    ${1 if register.is_external else 0}, 
                                    ${reg_dw}'h${"%x" % field.reset}, 
                                    ${1 if register.hwaccess in ["hrw", "hro"] else 0}, 
                                    ${1 if register.hwaccess == "hrw" else 0}, 
                                    1);
% endfor
    endfunction
  endclass

% endfor

endpackage