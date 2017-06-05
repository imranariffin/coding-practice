class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		if needle in haystack:
			return haystack.index(needle)
		return -1

if __name__=="__main__":
	s = Solution()
	print s.strStr("asdf", "")