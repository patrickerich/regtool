// Register block: ${name}
// Generated by reggen tool

module ${name}_reg_block #(
    parameter int RegWidth = ${regwidth}
) (
    input                      clk_i,
    input                      rst_ni,
    
    // Register interface
    input                      reg_we_i,
    input                      reg_re_i,
    input        [31:0]        reg_addr_i,
    input        [RegWidth-1:0] reg_wdata_i,
    output logic [RegWidth-1:0] reg_rdata_o,
    output logic               reg_error_o
);

% for register in registers:
    // ${register.name} Register
    logic [${regwidth-1}:0] ${register.name.lower()}_q;
    % if register.swaccess == "rw":
    logic ${register.name.lower()}_we;
    % endif
    
% endfor

    // Register write enables
% for register in registers:
    % if register.swaccess == "rw":
    assign ${register.name.lower()}_we = reg_we_i && (reg_addr_i == 'h${"%x" % register.offset});
    % endif
% endfor

    // Sequential write logic
% for register in registers:
    % if register.swaccess == "rw":
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            ${register.name.lower()}_q <= '0;
        end else if (${register.name.lower()}_we) begin
            ${register.name.lower()}_q <= reg_wdata_i;
        end
    end
    % endif
% endfor

    // Register read logic
    always_comb begin
        reg_rdata_o = '0;
        reg_error_o = 1'b0;
        
        case (reg_addr_i)
% for register in registers:
            'h${"%x" % register.offset}: reg_rdata_o = ${register.name.lower()}_q;
% endfor
            default: reg_error_o = 1'b1;
        endcase
    end

endmodule