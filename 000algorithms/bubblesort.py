"""
bubble sort:
author: imran
"""

def bubblesort(ls):
	n = len(ls)

	for k in range(n)[::-1]:
		if n-k < 2:
			pass
		for i,x in enumerate(ls[:k]):
			if x > ls[i+1]:
				ls[i], ls[i+1] = ls[i+1], ls[i]
	return

"""
Suite of Unit Tests
"""

import unittest

class TestBubbleSort(unittest.TestCase):

	def test_base_case(self):
		ls = [2,1]
		bubblesort(ls)
		self.assertEqual(ls, [1,2])

	def test_base_case_sorted(self):
		ls = [1,2]
		bubblesort(ls)
		self.assertEqual(ls, [1,2])

	def test_base_case_empty(self):
		ls = []
		bubblesort(ls)
		self.assertEqual(ls, [])

	def test_reverse_ordered(self):
		ls = [10, 9, 8, 5, 1]
		bubblesort(ls)
		self.assertEqual(ls, [1, 5, 8, 9, 10])

	def test_negative_ordered(self):
		ls = [-10,-9,-8,-5,-1]
		bubblesort(ls)
		self.assertEqual(ls, [-10,-9,-8,-5,-1])

	def test_negative_reverse_ordered(self):
		ls = [-1, -5, -8, -9, -10]
		bubblesort(ls)
		self.assertEqual(ls, [-10,-9,-8,-5,-1])

	def test_base_case_fractions(self):
		ls = [2.0, 1.0]
		bubblesort(ls)
		self.assertEqual(ls, [1.0, 2.0])

if __name__ == '__main__':
    unittest.main()