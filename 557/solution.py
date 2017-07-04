class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		return " ".join([w[::-1] for w in s.split(' ')])


if __name__ == '__main__':

	sol = Solution()

	print "TEST 0"
	s0 = "Let's take LeetCode contest"
	ret0 = sol.reverseWords(s0)
	print ret0
	assert ret0 == "s'teL ekat edoCteeL tsetnoc"