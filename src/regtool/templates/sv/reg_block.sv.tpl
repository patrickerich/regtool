// Register block: {{ name }}
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
    
    // External register interfaces
% for register in registers:
% if register.get('is_external', False):
    // ${register.name} external interface
    output logic            ${register.name.lower()}_req_o,
    output logic            ${register.name.lower()}_we_o,
    output logic [DW-1:0]   ${register.name.lower()}_wdata_o,
    input  logic [DW-1:0]   ${register.name.lower()}_rdata_i,
    input  logic            ${register.name.lower()}_ack_i,
% endif
% endfor
);

    // External register access
% for register in registers:
% if register.get('is_external', False):
    assign ${register.name.lower()}_req_o = (reg_addr_i == 'h${"%x" % register.offset});
    assign ${register.name.lower()}_we_o = ${register.name.lower()}_req_o && reg_we_i;
    assign ${register.name.lower()}_wdata_o = reg_wdata_i;
% endif
% endfor{% for register in registers %}
    // {{ register.name }} Register
    logic [DW-1:0] {{ register.name|lower }}_q;
    {% if register.swaccess == "rw" %}
    logic {{ register.name|lower }}_we;
    {% endif %}
    
{% endfor %}

    // Register read logic
    always_comb begin
        reg_rdata_o = '0;
        reg_error_o = 1'b0;
        
        case (reg_addr_i)
% for register in registers:
            'h${"%x" % register.offset}: reg_rdata_o = ${register.name.lower()}_q;
% for alias in register.get('aliases', []):
            'h${"%x" % alias}: reg_rdata_o = ${register.name.lower()}_q;  // Alias
% endfor
% endfor
            default: reg_error_o = 1'b1;
        endcase
    end

    // Register write enables
% for register in registers:
    % if register.swaccess == 'rw':
    assign ${register.name.lower()}_we = reg_we_i && (reg_addr_i == 'h${"%x" % register.offset}
% for alias in register.get('aliases', []):
                                        || reg_addr_i == 'h${"%x" % alias}
% endfor
                                        );
    % endif
% endfor    // Sequential write logic
% for register in registers:
    % if register.swaccess in ['rw', 'w1c', 'w1s']:
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            ${register.name.lower()}_q <= '0;
        end else if (${register.name.lower()}_we) begin
        % if register.swaccess == 'w1c':
            ${register.name.lower()}_q <= ~reg_wdata_i & ${register.name.lower()}_q;
        % elif register.swaccess == 'w1s':
            ${register.name.lower()}_q <= reg_wdata_i | ${register.name.lower()}_q;
        % else:
            ${register.name.lower()}_q <= reg_wdata_i;
        % endif
        end
    end
    % endif
% endfor

    // Register read logic
    always_comb begin
        reg_rdata_o = '0;
        reg_error_o = 1'b0;
        
        case (reg_addr_i)
{% for register in registers %}
            'h{{ "%x"|format(register.offset) }}: reg_rdata_o = {{ register.name|lower }}_q;
{% endfor %}
            default: reg_error_o = 1'b1;
        endcase
    end

endmodule