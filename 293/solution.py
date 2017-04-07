class Solution(object):
	def generatePossibleNextMoves(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		ret = set()
		for i in range(len(s)-1):
			if '-' not in s[i:i+2]:
				new_s = '%s%s%s'%(s[:i], '--', s[i+2:])
				ret.add(new_s)
		return list(ret)

if __name__ == '__main__':
	sol = Solution()

	print "TEST 0"
	s0 = "++++"
	print s0
	print sol.generatePossibleNextMoves(s0)

	print "TEST 1"
	s1 = "+++++"
	print s1
	print sol.generatePossibleNextMoves(s1)

	print "TEST 2"
	s2 = "+--++"
	print s2
	print sol.generatePossibleNextMoves(s2)