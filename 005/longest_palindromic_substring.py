class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		max_l = 0
		ret = ""
		l = len(s)
		for i in range(l):
			for j in range(i+1, l+1):
				substr = s[i:j]
				l_substr = len(substr)
				if self.is_palindrome(substr) and l_substr > max_l:
					max_l = l_substr
					ret = substr
		return ret

	# def get_all_substr(self, s):
	# 	ret = []
	# 	l = len(s)
	# 	for i in range(l):
	# 		for j in range(i+1, l+1):
	# 			ret.append(s[i:j])
	# 	return ret

	def is_palindrome(self, s):
		l = len(s)
		for i in range(l/2):
			if s[i] != s[l-i-1]:
				return False
		return True


if __name__=="__main__":
	s = Solution()
	# print s.get_all_substr("abcdef")
	print s.is_palindrome("aba")
	print s.is_palindrome("aa")
	print s.is_palindrome("abcba")
	print s.is_palindrome("accba")

	print s.longestPalindrome("aaaaaaab")