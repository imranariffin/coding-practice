import unittest

from BinaryTreeIteratorPreorder import BinaryTreeIteratorPreorder, TreeNode


class TestBinaryTreeIteratorPreorder(unittest.TestCase):
    def test_null(self):
        iter = BinaryTreeIteratorPreorder(None)

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
                [1,2,3,4,5,6],
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
                [1,2,3,4,5],
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
                [1,2,3,4,5],
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
                [1,2,3,4,6,5]
            ),
        ]

        for node, expected in testcases:
            iter = BinaryTreeIteratorPreorder(node)

            results = []
            while iter.hasnext():
                results.append(iter.next().val)

            self.assertEqual(results, expected, f'{results} != {expected}')


if __name__ == '__main__':
    unittest.main()
