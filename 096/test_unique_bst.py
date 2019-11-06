import unittest
from unique_bst import Solution


class TestUniqueBST(unittest.TestCase):
    def test(self):
        s = Solution()
        test_cases = [
            (1, 1),
            (2, 2),
            (3, 5),
            (4, 14),
            (5, 42),
            (6, 132),
            (7, 429),
        ]
        for n, want in test_cases:

            got = s.numTrees(n)

            self.assertEqual(got, want)


if __name__ == '__main__':
    unittest.main()
