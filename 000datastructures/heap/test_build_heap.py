import unittest

from heap import build_heap


class TestBuildMaxHeap(unittest.TestCase):
    def test_empty(self):
        ls = []

        build_heap(ls)

        self.assertEqual(ls, [])

    def test_already_heap(self):
        ls = [7, 5, 6, 4, 3, 2, 1]

        build_heap(ls)

        self.assertEqual(ls, [7, 5, 6, 4, 3, 2, 1])

    def test_unordered(self):
        """
           ┌──2
           │
        ┌──7
        │  └──5
        6
        │     ┌──6
        │  ┌──3
        │  │  └──9
        └──8
           │  ┌──3
           └──7
              └──2
        build_heap()
           ┌──2
           │
        ┌──7
        │  └──5
        9
        │     ┌──6
        │  ┌──6
        │  │  └──3
        └──8
           │  ┌──3
           └──7
              └──2
        """
        ls = [6, 8, 7, 7, 3, 5, 2, 2, 3, 9, 6]

        build_heap(ls)

        self.assertEqual(ls, [9, 8, 7, 7, 6, 5, 2, 2, 3, 3, 6])


if __name__ == '__main__':
    unittest.main()
