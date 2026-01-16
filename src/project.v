`default_nettype none

module tt_um_taghreed_eialsalman_half_adder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire A = ui_in[0];
    wire B = ui_in[1];

    wire Sum   = A ^ B;
    wire Carry = A & B;

    assign uo_out[0] = Sum;
    assign uo_out[1] = Carry;
    assign uo_out[7:2] = 6'b0;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    wire _unused = &{ena, clk, rst_n, ui_in[7:2], uio_in, 1'b0};

endmodule
