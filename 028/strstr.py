class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		i = 0
		j = len(needle)
		l = len(haystack)

		if j > l:
			return -1

		for i in range(l-j+1):
			print haystack[i:j]

			if needle == haystack[i:j]:
				return i

			i += 1
			j += 1

		return -1

if __name__=="__main__":
	s = Solution()
	print s.strStr("asdf", "")