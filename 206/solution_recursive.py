# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

# recursive
class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None: return None
		return self.__reverseList(None, head, head.next)

	def __reverseList(self, prev, curr, next):
		"""
		:type prev, curr, next: ListNode
		:type head: ListNode
		:rtype: ListNode
		"""
		if not next:
			curr.next = prev
			return curr

		curr.next = prev
		return self.__reverseList(curr, next, next.next)

def ll_print(ll):
	while ll:
		print ll.val,
		ll = ll.next
	print ""

if __name__ == '__main__':
	s = Solution()
	l1 = ListNode(1)
	l1.next = ListNode(2)
	l1.next.next = ListNode(3)
	l1.next.next.next = ListNode(4)
	l1.next.next.next.next = ListNode(5)

	l2 = ListNode(1)

	l3 = ListNode(1)
	l3.next = ListNode(2)

	l4 = None

	ll_print(l1)
	ll_print(s.reverseList(l1))

	ll_print(l2)
	ll_print(s.reverseList(l2))

	ll_print(l3)
	ll_print(s.reverseList(l3))

	ll_print(l4)
	ll_print(s.reverseList(l4))