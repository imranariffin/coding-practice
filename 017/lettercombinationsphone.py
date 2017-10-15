class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.letters = {
            "1": "*", "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        self. ret = []
        self.bt(0, digits, [])
        return self.ret
        
    def bt(self, i, digits, comb):
        if i == len(digits):
            if comb:
                self.ret.append("".join(comb))
            return
        d = digits[i]
        for c in self.letters[d]:
            self.bt(i + 1, digits, list(comb + [c]))
