# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def dfsVisit(self, V, node):
        for v in node.neighbors:
            if not V.has_key(v.label):
                V[v.label] = UndirectedGraphNode(v.label)
                self.dfsVisit(V, v)
                
            V[node.label].neighbors.append(V[v.label])
            
        return
    
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        
        V = dict()
        
        V[node.label] = UndirectedGraphNode(node.label)
        self.dfsVisit(V, node)
        
        return V[node.label]
