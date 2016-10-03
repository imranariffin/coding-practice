class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		counter = dict()
		for c in s:
			if c in counter:
				counter[c] += 1
			else:
				counter[c] = 1

		return self.n_even_chars(counter) + self.n_max_odd_chars(counter)

	def n_even_chars(self, counter):
		ret = 0
		for c, f in counter.iteritems():
			if f%2==0:
				ret += f

		return ret

	def n_max_odd_chars(self, counter):
		ret = 0
		max_char = ''
		for c, f in counter.iteritems():
			if f%2==1:
				if ret < f:
					ret = f
					max_char = c

		if max_char in counter:
			del counter[max_char]

		for c, f in counter.iteritems():
			if f%2==1:
				ret += f-1

		return ret


if __name__=="__main__":
	s = Solution()
	print s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
	# print s.longestPalindrome("abccccdd")