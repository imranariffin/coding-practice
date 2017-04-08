import math

class Solution(object):
	def constructRectangle(self, area):
		"""
		:type area: int
		:rtype: List[int]
		"""
		mindiff = area
		W, L = 1, area
		for i in range(2, int(math.sqrt(area))+1):
			if area%i == 0:
				w, l = i, area/i
				if l - w < mindiff:
					mindiff = l - w
					W, L = w, l
		return [L, W]


if __name__ == '__main__':
	sol = Solution()

	area0 = 4
	ret0 = sol.constructRectangle(area0)
	print ret0
	assert ret0 == [2, 2]

	area0 = 8
	ret0 = sol.constructRectangle(area0)
	print ret0
	assert ret0 == [4, 2]