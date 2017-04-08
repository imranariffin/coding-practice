import sys

class Solution(object):
	def shortestDistance(self, words, word1, word2):
		"""
		:type words: List[str]
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		ret = sys.maxint
		for i, w in enumerate(words):
			if w == word1:
				li = self.maxindex(words[:i], word2) if word2 in words[:i] else sys.maxint
				ri = words.index(word2, i+1) if word2 in words[i+1:] else sys.maxint
				cur = min(abs(i - li), abs(ri - i))
				if cur < ret:
					ret = cur
		return ret

	def maxindex(self, ls, e):
		return max([i for i,x in enumerate(ls) if x==e])

if __name__ == '__main__':
	sol = Solution()

	print "TEST maxindex0"
	ls = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
	ret = sol.maxindex(ls, 'd')
	print ret
	assert ret == len(ls)-1

	print "TEST maxindex0"
	ls = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
	ret = sol.maxindex(ls, 'a')
	print ret
	assert ret == 4

	print "TEST0"
	words0 = ["practice", "makes", "perfect", "coding", "makes"]
	w1_0, w2_0 = "coding", "practice"
	ret0 = sol.shortestDistance(words0, w1_0, w2_0)
	print ret0
	assert ret0 == 3

	print "TEST4"
	words4 = ["coding", "makes", "perfect", "practice", "makes"]
	w1_4, w2_4 = "coding", "practice"
	ret4 = sol.shortestDistance(words4, w1_4, w2_4)
	print ret4
	assert ret4 == 3

	print "TEST1"
	words1 = ["practice", "makes", "perfect", "coding", "makes"]
	w1_1, w2_1 = "makes", "coding"
	ret1 = sol.shortestDistance(words1, w1_1, w2_1)
	print ret1
	assert ret1 == 1

	print "TEST2"
	words2 = ["a", "b", "c", "c", "b"]
	w1_2, w2_2 = "a", "b"
	ret2 = sol.shortestDistance(words2, w1_2, w2_2)
	print ret2
	assert ret2 == 1

	print "TEST3"
	words3 = ["a", "b", "c", "c", "b"]
	w1_3, w2_3 = "b", "a"
	ret3 = sol.shortestDistance(words3, w1_3, w2_3)
	print ret3
	assert ret3 == 1

	print "TEST5"
	words5 = ["a","c","a","b"]
	w1_5, w2_5 = "b", "a"
	ret5 = sol.shortestDistance(words5, w1_5, w2_5)
	print ret5
	assert ret5 == 1