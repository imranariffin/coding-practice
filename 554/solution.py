import sys

class Solution(object):
	def leastBricks(self, wall):
		"""
		:type wall: List[List[int]]
		:rtype: int
		"""
		if not wall:
			return 0
		h = len(wall)
		w = sum(wall[0])

		c = dict()
		for row in wall:
			s = 0
			for e in row[:-1]:
				s += e
				if s not in c:
					c[s] = 1
				else:
					c[s] += 1
		if not c: return h
		return h - max([c[e] for e in c])

if __name__ == '__main__':
	sol = Solution()

	print "TEST 0"
	wall0 = [
		[1,2,2,1],
		[3,1,2],
		[1,3,2],
		[2,4],
		[3,1,2],
		[1,3,1,1]
	]
	for row in wall0: print row
	ret0 = sol.leastBricks(wall0)
	print ret0
	# assert ret0 == 2

	wall1 = [
		[1,2,2,1],
		[3,1,2],
		[1,3,2],
		[2,4],
		[3,1,2],
		[1,3,1,1]
	]
	for row in wall1: print row