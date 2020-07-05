module top_ver (q, p, r, out);

    input     q, p, r;
    output    [1:0] out;
    reg     out, intsig;

    bottom1 u1(.a(q), .b(p), .c(intsig));
    bottom2 u2(.l(intsig), .m(r), .n(out));

endmodule
