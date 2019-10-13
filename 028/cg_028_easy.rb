# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
    return  0 if needle.empty?
    (0...haystack.length).each do |i|
        break if (i + needle.length) > haystack.length
        return i if haystack[i, needle.length] == needle
    end
    -1
end
