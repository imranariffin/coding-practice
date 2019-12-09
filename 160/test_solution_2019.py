import unittest

from solution_2019 import Solution, ListNode


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def createListNode(self, ls) -> ListNode:
        for i, node in enumerate(ls):
            node.next = ls[i+1] if i < len(ls)-1 else None
        return ls[0] if len(ls) > 0 else None

    def test(self):
        list_a = [ListNode(n) for n in [4,1,8,4,5]]
        list_b = [ListNode(n) for n in [5,0,1,8,4,5]]
        ix = ListNode(8)
        list_a[2] = ix
        list_b[3] = ix
        headA = self.createListNode(list_a)
        headB = self.createListNode(list_b)
        want = ix

        got = self.s.getIntersectionNode(headA, headB)

        assert got == want, f'{got} != {want}'

    def test_two(self):
        list_a = [ListNode(n) for n in [0,9,1,2,4]]
        list_b = [ListNode(n) for n in [3,2,4]]
        ix = ListNode(2)
        list_a[3] = ix
        list_b[1] = ix
        headA = self.createListNode(list_a)
        headB = self.createListNode(list_b)
        want = ix

        got = self.s.getIntersectionNode(headA, headB)

        assert got == want, f'{got} != {want}'

    def test_three(self):
        list_a = [ListNode(n) for n in [2,6,4]]
        list_b = [ListNode(n) for n in [1,5]]
        headA = self.createListNode(list_a)
        headB = self.createListNode(list_b)
        want = None

        got = self.s.getIntersectionNode(headA, headB)

        assert got == want, f'{got} != {want}'


if __name__ == '__main__':
    unittest.main()

