# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    return true if s.empty?
    i1 = 0
    i2 = s.length - 1
    while i1 < i2
        if i1 < s.length && !(s[i1] =~ /[A-Za-z0-9]/)
            i1 += 1
            next
        end
        if i2 >= 0 && !(s[i2] =~ /[A-Za-z0-9]/)
            i2 -= 1
            next
        end
        return false if s[i1].downcase != s[i2].downcase
        i1 += 1
        i2 -= 1
    end
    true
end
