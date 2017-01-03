# @param {String} s
# @return {Integer}
def length_of_last_word(s)
    s_last = s.split(" ")[-1]
    
    if s_last == nil
        return 0
    end
    
    return s_last.length
end
