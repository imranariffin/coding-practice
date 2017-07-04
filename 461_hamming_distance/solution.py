class Solution(object):
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """

    xor = x ^ y
    hamming_dist = 0

    while xor:
    	hamming_dist += xor & 1
    	xor = (xor >> 1)

    return hamming_dist

if __name__ == '__main__':
	"""
	TEST CASES
	"""
	s = Solution()
	
	# HD(100, 001) => 2
	assert(s.hammingDistance(4, 1) == 2)
	# HD(1000, 0001) => 2
	assert(s.hammingDistance(8, 1) == 2)
	# HD(1000, 0000) => 1
	assert(s.hammingDistance(8, 0) == 1)
	# HD(0000, 0000) => 0
	assert(s.hammingDistance(0, 0) == 0)
	# HD(01010, 10101) => 5
	assert(s.hammingDistance(10, 21) == 5)