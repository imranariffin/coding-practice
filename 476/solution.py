from math import log, pow

class Solution(object):
	def findComplement(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		mask = int(pow(2, int(log(num, 2)) + 1) - 1)
		ret = ((~num) & mask)
		# print num, "{0:b}".format(num), mask, "{0:b}".format(ret)
		return ret

if __name__ == '__main__':
	s = Solution()

	for n in range(1, 17):
		s.findComplement(n)