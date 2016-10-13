# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
            
        Q = []
        V = dict()
        
        Q.append(node)
        V[node.label] = UndirectedGraphNode(node.label)
        
        while Q:
            u = Q.pop(0)
            
            for v in u.neighbors:
                if not V.has_key(v.label):
                    Q.append(v)
                    V[v.label] = UndirectedGraphNode(v.label)
                    
                V[u.label].neighbors.append(V[v.label])
                
        return V[node.label]
