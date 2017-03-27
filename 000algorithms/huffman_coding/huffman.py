from collections import Counter
import heapq

class TreeNode:
	def __init__(self, char=None, freq=0, left=None, right=None):
		self.char = char
		self.freq = freq
		self.left = left
		self.right = right

	def __str__(self):
		return "<{},{}>".format(self.char, self.freq)

	def __repr__(self):
		return "<{},{}>".format(self.char, self.freq)

	def __lt__(self, other):
		return self.freq < other.freq

	def inordertraverse(self):
		if self==None:
			return
		self.__inordertraverse__(1)

	def __inordertraverse__(self, depth):
		if self.right != None:
			self.right.__inordertraverse__(depth+1)
		if self.char == None:
			print "----"*depth, "X", self.freq
		else:
			print "----"*depth, self.char, self.freq
		if self.left != None:
			self.left.__inordertraverse__(depth+1)

def compress(s):
	"""
	Given string, create huffman tree
	@params s: String
	rtype: TreeNode
	"""
	freqs = Counter()
	for c in s:
		freqs[c] += 1

	print freqs

	q = [TreeNode(char=c, freq=freqs[c], left=None, right=None) for c in freqs]

	print q

	heapq.heapify(q)

	print q

	while len(q) > 1:
		print q

		leftT = heapq.heappop(q)
		rightT = heapq.heappop(q)
		t = TreeNode(freq=leftT.freq+rightT.freq, left=leftT, right=rightT)

		heapq.heappush(q, t)

	print q

	return heapq.heappop(q)

def decompress(t):

	

if __name__ == '__main__':

	print "TEST-1: inorder traverse balanced tree"
	t = TreeNode('d', 4, 
		TreeNode('b', 2,
			TreeNode('a', 1, 
				None, 
				None),
			TreeNode('c', 3,
				None,
				None)),
		TreeNode('f', 6,
			TreeNode('f', 5, 
				None,
				None),
			TreeNode('g', 7, 
				None,
				None)))
	t.inordertraverse()

	s0 = 'abbbcaaaa'
	print ""
	print "TEST0: huffman({})".format(s0)
	res0 = compress(s0)
	res0.inordertraverse()


	s1 = 'abcaaaaaabdefghhiiiaaaa'
	print ""
	print "TEST1: huffman({})".format(s1)
	res1 = compress(s1)
	res1.inordertraverse()

	s2 = "this is an example of a huffman tree"
	print ""
	print "TEST2: huffman({})".format(s2)
	res2 = compress(s2)
	res2.inordertraverse()