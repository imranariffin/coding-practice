# @param {Integer} x
# @return {Integer}
def reverse(x)
    x_string = x.to_s
    x_string = x_string[0] == "-" ? x_string[0] + x_string[1..-1].reverse : x_string.reverse
    x_i = x_string.to_i
    x_i = (x_i <= 2147483647 && x_i >= -2147483648) ? x_i : 0
end
