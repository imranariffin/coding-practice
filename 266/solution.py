from collections import Counter

class Solution(object):
	def canPermutePalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		wc = Counter()

		for c in s:
			wc[c] += 1

		n_odds = 0
		for c in wc.keys():
			if wc[c]%2 != 0:
				n_odds += 1

		if len(wc) > 1:
			return (n_odds < 2)
		return True

if __name__ == '__main__':
	s = Solution()

	w = "aba"
	print w
	assert(s.canPermutePalindrome(w) == True)

	w = "abba"
	print w
	assert(s.canPermutePalindrome(w) == True)

	w = "abbac"
	print w
	assert(s.canPermutePalindrome(w) == True)

	w = "abbacccddd"
	print w
	assert(s.canPermutePalindrome(w) == False)

	w = "aaa"
	print w
	assert(s.canPermutePalindrome(w) == True)

	w = "aaaabbb"
	print w
	assert(s.canPermutePalindrome(w) == True)

	w = "as"
	print w
	assert(s.canPermutePalindrome(w) == False)

	w = "asb"
	print w
	assert(s.canPermutePalindrome(w) == False)

	w = "abcd"
	print w
	assert(s.canPermutePalindrome(w) == False)

	w = "as"
	print w
	assert(s.canPermutePalindrome(w) == False)

	w = "as"
	print w
	assert(s.canPermutePalindrome(w) == False)