class Solution(object):

	def is_path(self, s):
		for c in s:
			if c == '.': return True
		return False

	def lengthLongestPath(self, input):
		"""
		:type input: str
		:rtype: int
		"""
		ls_nodes = [(s.strip('\t') + '/', len(s) - len(s.strip('\t'))) for s in input.split('\n')]
		ls_filepaths = []

		parents = dict()
		for i, node in enumerate(ls_nodes):

			d = node[1]
			parents[d] = i

			if d != 0:
				parent = ls_nodes[parents[d - 1]]
				ls_nodes[i] = (parent[0] + node[0], node[1])

			if self.is_path(ls_nodes[i][0]):
				ls_filepaths.append((ls_nodes[i][0], len(ls_nodes[i][0])))

# 		print ls_filepaths

		# count path length
		for i, node in enumerate(ls_nodes):
			ls_nodes[i] = (node[0], len(node))

		# get longest
		max_length = 0
		longest_path = ""
		for file in ls_filepaths:
			if file[1] > max_length:
				max_length = file[1]
				longest_path = file[0]

		print longest_path
		return max_length - 1 if max_length > 0 else 0

if __name__ == '__main__':
	s = Solution()
	s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
	s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")