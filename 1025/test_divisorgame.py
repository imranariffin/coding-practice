import unittest
from divisorgame import Solution

class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_00(self):
        n = 1
        got = self.s.divisorGame(n)
        self.assertEqual(got, False)

    def test_01(self):
        n = 2
        got = self.s.divisorGame(n)
        self.assertEqual(got, True)

    def test_02(self):
        n = 3
        got = self.s.divisorGame(n)
        self.assertEqual(got, False)

    def test_03(self):
        n = 4
        got = self.s.divisorGame(n)
        self.assertEqual(got, True)

    def test_04(self):
        n = 5
        got = self.s.divisorGame(n)
        self.assertEqual(got, False)

    def test_05(self):
        n = 6
        got = self.s.divisorGame(n)
        self.assertEqual(got, True)

if __name__ == '__main__':
    unittest.main()
