// Register block: ${name}
// Generated by regtool

module ${name}_reg_block #(
    parameter int AW = ${reg_aw},
    parameter int DW = ${reg_dw}
) (
    input                    clk_i,
    input                    rst_ni,
    
    // Register interface
    input                    reg_we_i,
    input                    reg_re_i,
    input        [AW-1:0]    reg_addr_i,
    input        [DW-1:0]    reg_wdata_i,
    output logic [DW-1:0]    reg_rdata_o,
    output logic             reg_error_o,

    // Field outputs
% for register in registers:
% for field in register.fields:
    output logic [${field.width-1}:0] ${register.name.lower()}_${field.name.lower()}_o,
% endfor
% endfor

    // External register interface
% for register in registers:
% if register.is_external:
    input        [DW-1:0]    ${register.name.lower()}_i,
% endif
% endfor

    // Hardware access interface
% for register in registers:
% if register.hwaccess == "hrw":
    input        [DW-1:0]    ${register.name.lower()}_wr_data_i,
    input                    ${register.name.lower()}_wr_en_i,
% endif
% if register.hwaccess in ["hrw", "hro"]:
    output logic [DW-1:0]    ${register.name.lower()}_rd_data_o,
% endif
% endfor
);

% for register in registers:
    // ${register.name} Register
% if not register.is_external:
    logic [DW-1:0] ${register.name.lower()}_q;
% endif
    % if register.swaccess == "rw":
    logic ${register.name.lower()}_we;
    % endif
    
% endfor

    // Register write enables
% for register in registers:
    % if register.swaccess == "rw":
    assign ${register.name.lower()}_we = reg_we_i && (reg_addr_i == 'h${"%x" % register.offset}
% for alias in register.get('aliases', []):
                                        || reg_addr_i == 'h${"%x" % alias}
% endfor
                                        );
    % endif
% endfor

    // Sequential write logic with reset values
% for register in registers:
% if not register.is_external:
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            // Reset each field to its specified value
% for field in register.fields:
            ${register.name.lower()}_q[${field.msb}:${field.lsb}] <= ${field.width}'h${"%x" % field.reset};
% endfor
        end else begin
            if (${register.name.lower()}_we) begin
                // Software write operation
% for field in register.fields:
                ${register.name.lower()}_q[${field.msb}:${field.lsb}] <= reg_wdata_i[${field.msb}:${field.lsb}];
% endfor
            end
% if register.hwaccess == "hrw":
            else if (${register.name.lower()}_wr_en_i) begin
                // Hardware write operation
                ${register.name.lower()}_q <= ${register.name.lower()}_wr_data_i;
            end
% endif
        end
    end

    // Field output assignments
% for field in register.fields:
    assign ${register.name.lower()}_${field.name.lower()}_o = ${register.name.lower()}_q[${field.msb}:${field.lsb}];
% endfor

% if register.hwaccess in ["hrw", "hro"]:
    // Hardware read access
    assign ${register.name.lower()}_rd_data_o = ${register.name.lower()}_q;
% endif
% endif
% endfor

    // Register read logic
    always_comb begin
        reg_rdata_o = '0;
        reg_error_o = 1'b0;
        
        case (reg_addr_i)
% for register in registers:
            'h${"%x" % register.offset}: reg_rdata_o = ${register.is_external ? register.name.lower() + '_i' : register.name.lower() + '_q'};
% for alias in register.get('aliases', []):
            'h${"%x" % alias}: reg_rdata_o = ${register.is_external ? register.name.lower() + '_i' : register.name.lower() + '_q'};  // Alias
% endfor
% endfor
            default: reg_error_o = 1'b1;
        endcase
    end

endmodule
