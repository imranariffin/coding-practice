# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0]
        def dfs(node) -> int:
            if node is None:
                return 0
            lh = dfs(node.left)
            rh = dfs(node.right)
            diameter[0] = max(diameter[0], lh + rh)
            return 1 + max(lh, rh)

        dfs(root)

        return diameter[0]


if __name__ == '__main__':
    import unittest

    class Test(unittest.TestCase):
        def test(self):
            testcases = [
                {
                    'tree': TreeNode(
                        1,
                        TreeNode(
                            2,
                            TreeNode(4),
                            TreeNode(5),
                        ),
                        TreeNode(3),
                    ),
                    'expected': 3,
                },
                {
                    'tree': TreeNode(
                        1,
                        TreeNode(
                            2,
                            TreeNode(
                                4,
                                TreeNode(5),
                            ),
                            TreeNode(
                                6,
                                None,
                                TreeNode(7),
                            ),
                        ),
                        TreeNode(3),
                    ),
                    'expected': 4,
                },
                {
                    'tree': None,
                    'expected': 0,
                },
            ]
            s = Solution()

            for t in testcases:
                self.assertEqual(s.diameterOfBinaryTree(t['tree']), t['expected'])


    unittest.main()

