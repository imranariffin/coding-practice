import unittest

from heap import heapify


class TestHeapify(unittest.TestCase):
    def test_empty_list(self):
        ls = []

        heapify(ls, 0)

        self.assertEqual(ls, [])
    
    def test_already_max_heap(self):
        """
        ┌──1
        3
        └──2
        heapify()
        ┌──1
        3
        └──2
        """
        ls = [3, 2, 1]

        heapify(ls, 0)

        self.assertEqual(ls, [3, 2, 1])

    def test_unordered_list(self):
        """
        ┌──3
        2
        └──1
           └──0
        heapify()
        ┌──2
        3
        └──1
           └──0
        """
        ls = [2, 1, 3, 0]

        heapify(ls, 0)

        self.assertEqual(ls, [3, 1, 2, 0])
    
    def test_unordered_list_negative(self):
        """
        ┌── 0
        -1
        └──-2
            └──-3
        heapify()
        ┌──-1
        0
        └──-2
            └──-3
        """
        ls = [-1, -2, 0, -3]

        heapify(ls, 0)

        self.assertEqual(ls, [0, -2, -1, -3])

    def test_unordered_list_2(self):
        """
           ┌──10
           │
        ┌──8
        │  └──2
        7
        │  ┌──9
        │  │
        └──3
           │  ┌──1
           └──1
              └──11
        heapify()
           ┌──7
           │
        ┌──10
        │  └──2
        8
        │  ┌──9
        │  │
        └──3
           │  ┌──1
           └──1
              └──11
        """
        ls = [7, 3, 8, 1, 9, 2, 10, 11, 1]

        heapify(ls, 0)

        self.assertEqual(ls, [8, 3, 10, 1, 9, 2, 7, 11, 1])


if __name__ == '__main__':
    unittest.main()
