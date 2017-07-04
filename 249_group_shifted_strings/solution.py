import string

class Solution(object):
	char_map = {char:i for (i, char) in enumerate(string.ascii_lowercase)}

	def groupStrings(self, strings):
		"""
		:type strings: List[str]
		:rtype: List[List[str]]
		"""
		strings = set(strings)
		ret = []
		
		while len(strings):
			s1 = strings.pop()
			g = [s1]
			for s2 in list(strings):
				if self.is_same_group(s1, s2):
					g.append(s2)
					strings.discard(s2)

			ret.append(g)

		return ret


	def get_shift(self, c1, c2):
		return self.char_map[c1] - self.char_map[c2]

	def is_same_group(self, s1, s2):
		len1 = len(s1)
		len2 = len(s2)
		if len1 != len2: return False
		if not len1 or len1 == 1: return True

		shift = self.get_shift(s1[0], s2[0])
		for i in range(1, len1):
			if shift != self.get_shift(s1[i], s2[i]):
				return False

		return True


if __name__ == '__main__':
	s = Solution()

	# tests for is_same_group
	assert(s.is_same_group("abc", "bcd")==True)
	assert(s.is_same_group("abc", "abc")==True)
	assert(s.is_same_group("", "")==True)
	assert(s.is_same_group("a", "z")==True)
	assert(s.is_same_group("xyz", "abc")==True)
	assert(s.is_same_group("xyz", "bcd")==True)
	assert(s.is_same_group("abc", "xyz")==True)
	assert(s.is_same_group("abc", "zyx")==False)
	assert(s.is_same_group("abc", "ace")==False)

	# tests for groupStrings
	assert(s.groupStrings(['abc'])==[['abc']])
	assert(set(s.groupStrings(['abc', 'bcd'])[0])==set(['abc', 'bcd']))
	assert(len(s.groupStrings(['abc', 'bcd']))==1)

	print s.groupStrings(['abc', 'acd'])
	print len([['abc'], ['acd']])
	assert(set(s.groupStrings(['abc', 'acd'])[0])==set(['abc']))
	assert(set(s.groupStrings(['abc', 'acd'])[1])==set(['acd']))
	print s.groupStrings(['abc', 'bcd'])