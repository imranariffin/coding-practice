# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

# iterative
class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None: return None
		if head.next == None: return head

		prev = None
		curr = head
		next = curr.next

		while next:
			curr.next = prev

			prev = curr
			curr = next
			next = curr.next

		curr.next = prev

		return curr

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