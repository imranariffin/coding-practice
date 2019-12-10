class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        traversal = []
        visited = {}
        stack = [root]

        while stack:
            node = stack[-1]
            if node not in visited:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                visited[node] = 1
                continue
            if visited[node] == 1:
                visited[node] += 1
                continue
            if visited[node] >= 2:
                traversal.append(node.val)
                stack.pop()

        return traversal

