# import collections

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
# 	def __init__(self, x):
# 		self.label = x
# 		self.neighbors = []

# class Queue(object):
# 	def __init__(self):
# 		self.q = []

# 	def __str__(self):
# 		return "".join([x for x in self.q])

# 	def push(self, x):
# 		self.q.append(x)

# 	def pop(self):
# 		return self.q.pop(0)

# 	def empty(self):
# 		return len(self.q) == 0

# # BFS solution (82 ms)
# class Solution(object):
# 	def cloneGraph(self, node):
# 		"""
# 		:type node: UndirectedGraphNode
# 		:rtype: UndirectedGraphNode
# 		"""
# 		if node == None:
# 			return None

# 		# create empty queue
# 		queue = Queue()
# 		# create empty visit set
# 		visited = set()
# 		# cloned set
# 		cloned = dict()

# 		queue.push(node)
# 		while not queue.empty():
# 			curr_node = queue.pop()
# 			if curr_node not in cloned:
# 				cloned[curr_node] = UndirectedGraphNode(curr_node.label)

# 			if curr_node not in visited:
# 				visited.add(curr_node)

# 				for n in curr_node.neighbors:
# 					if n not in visited:
# 						queue.push(n)

# 		for n1 in cloned.keys():
# 			cloned[n1].neighbors = [cloned[x] for x in n1.neighbors]

# 		return cloned[node]

# BFS solution (82 ms)
class Solution(object):
	def cloneGraph(self, node):
		"""
		:type node: UndirectedGraphNode
		:rtype: UndirectedGraphNode
		"""
		if node == None:
			return None

		cloned = dict()
		self.clonegraph_dfs(node, cloned)

		for n1 in cloned:
			cloned[n1].neighbors = [cloned[x] for x in n1.neighbors]
		return cloned[node]

	def clonegraph_dfs(self, node, cloned):
		assert(node != None)

		if node in cloned:
			return

		cloned[node] = UndirectedGraphNode(node.label)
		for n in node.neighbors:
			self.clonegraph_dfs(n, cloned)