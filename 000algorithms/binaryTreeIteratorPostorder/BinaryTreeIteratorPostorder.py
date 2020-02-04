# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        left = self.left.val if self.left else 'None'
        right = self.right.val if self.right else 'None'
        return f'Node({self.val},{left},{right})'
    
    def __repr__(self):
        return self.__str__()


class BinaryTreeIteratorPostorder:
    def __init__(self, root):
        self.stack = []
        self.visited = {}
        if not root:
            return
        self.stack.append(root)

    def hasnext(self):
        return len(self.stack) > 0
    
    def next(self):
        node = self.stack[-1]

        while self.stack:
            if self.visited.get(node, 0) == 2:
                self.stack.pop()
                break
            elif self.visited.get(node, 0) == 1:
                self.visited[node] = 2
                if node.right:
                    self.stack.append(node.right)
            elif self.visited.get(node, 0) == 0:
                self.visited[node] = 1
                if node.left:
                    self.stack.append(node.left)
            node = self.stack[-1]

        return node