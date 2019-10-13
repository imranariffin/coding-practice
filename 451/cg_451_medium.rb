# @param {String} s
# @return {String}
def frequency_sort(s)
    char_freq_hash = {}
    
    s.each_char do |ch|
        if !char_freq_hash.has_key?(ch)
            char_freq_hash[ch] = 0
        end
        
        char_freq_hash[ch] += 1
    end
    
    char_freq_hash = char_freq_hash.sort_by {|key, value| value}.reverse.to_h
    
    result = ""
    
    char_freq_hash.each do |key, value|
        result += key * value
    end
    
    return result
end
