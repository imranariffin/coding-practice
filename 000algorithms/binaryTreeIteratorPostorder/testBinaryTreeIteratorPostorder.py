import unittest

from BinaryTreeIteratorPostorder import BinaryTreeIteratorPostorder, TreeNode


class TestBinaryTreeIteratorPreorder(unittest.TestCase):
    def test_null(self):
        iter = BinaryTreeIteratorPostorder(None)

        results = []
        while iter.hasnext():
            results.append(iter.next().val)

        self.assertEqual(results, [])
    
    def test_all(self):
        testcases = [
            (
                TreeNode(
                    1,
                    TreeNode(
                        2,
                        TreeNode(
                            3,
                            TreeNode(4),
                        ),
                    ),
                    TreeNode(
                        5,
                        TreeNode(6)
                    )
                ),
                [4,3,2,6,5,1]
            ),
            (
                TreeNode(
                    1,
                    TreeNode(
                        2,
                        TreeNode(
                            3,
                            TreeNode(
                                4,
                                None,
                                TreeNode(5)
                            ),
                        ),
                    ),
                ),
                [5,4,3,2,1],
            ),
            (
                TreeNode(
                    1,
                    None,
                    TreeNode(
                        2,
                        None,
                        TreeNode(
                            3,
                            None,
                            TreeNode(
                                4,
                                TreeNode(5)
                            ),
                        ),
                    ),
                ),
                [5,4,3,2,1],
            ),
            (
                TreeNode(
                    1,
                    None,
                    TreeNode(
                        2,
                        TreeNode(
                            3,
                            TreeNode(
                                4,
                                None,
                                TreeNode(6),
                            ),
                            TreeNode(5),
                        ),
                        None,
                    ),
                ),
                [6,4,5,3,2,1]
            ),
        ]

        for node, expected in testcases:
            iter = BinaryTreeIteratorPostorder(node)

            results = []
            while iter.hasnext():
                results.append(iter.next().val)

            self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
