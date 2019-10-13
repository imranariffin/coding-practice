# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    return "" if strs.empty?
    s_arr_sorted = strs.sort
    l_c_p = 0
    for i in 0...s_arr_sorted[0].length do
        p = true
        s_arr_sorted.each { |s| p = false if s[i] != s_arr_sorted[0][i] }
        break if !p
        l_c_p += 1
    end
    s_arr_sorted[0][0, l_c_p]
end
