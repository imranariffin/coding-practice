class Solution:
    def maximum69Number (self, num: int) -> int:
        numstr = str(num)
        for i, d in enumerate(numstr):
            if d == '6':
                return int(numstr[:i] + '9' + numstr[i+1:])
        return num
