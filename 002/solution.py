# Definition for singly-linked list.
# class ListNode(object):
# 	def __init__(self, x, next):
# 		self.val = x
# 		self.next = next

class Solution(object):
	def ll_len(self, ll):
		ret = 0
		node = ll
		while node:
			node = node.next
			ret += 1
		return ret

	def ll_print(self, ll):
		node = ll
		while node:
			print node.val,
			node = node.next
		print ""

	# def ll_reverse(self, ll):
	# 	if ll == None: return None
	# 	if ll.next == None: return ll

	# 	node = ll.next
	# 	prev_node = ListNode(ll.val)
	# 	curr_node = ListNode(node.val)
	# 	curr_node.next = prev_node
	# 	node = node.next

	# 	while node:
	# 		prev_node = curr_node
	# 		curr_node = ListNode(node.val)
	# 		curr_node.next = prev_node
	# 		node = node.next

	# 	return curr_node

	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		# print ll_len(l1)
		# print ll_len(l1)

		len1 = self.ll_len(l1)
		len2 = self.ll_len(l2)

		if len1 < len2:
			temp = len1
			len1 = len2
			len2 = temp

			temp = l1
			l1 = l2
			l2 = temp

		# l1 = self.ll_reverse(l1)
		# l2 = self.ll_reverse(l2)

		# create ret list
		ret = ListNode(0)
		node = ret
		for i in range(1, len1):
			node.next = ListNode(0)
			node = node.next

		c = 0
		node1 = l1
		node2 = l2
		node = ret
		for i in range(len1):
			if i < len2:
				node.val = (c + node1.val + node2.val)%10
				c = 1 if c + node1.val + node2.val > 9 else 0
				node2 = node2.next
			else:
				node.val = (c + node1.val )%10
				c = 1 if c + node1.val > 9 else 0

			# last carry
			if i == len1 - 1 and c:
				node.next = ListNode(c)
			else:
				node = node.next
				node1 = node1.next

		# ret = self.ll_reverse(ret)
		return ret

# if __name__ == '__main__':
# 	l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
# 	l2 = ListNode(0, ListNode(0, ListNode(0, ListNode(1, None))))
# 	l3 = ListNode(1, None)
# 	l4 = None
# 	l8 = ListNode(0, ListNode(0, ListNode(0, ListNode(6, None))))
# 	l9 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
# 	l10 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
# 	s = Solution()

# 	print "=== TEST ll_print ==="
# 	s.ll_print(l1)
# 	print "length: ", s.ll_len(l1)
# 	s.ll_print(l2)
# 	print "length: ", s.ll_len(l2)
# 	s.ll_print(l3)
# 	print "length: ", s.ll_len(l3)
# 	s.ll_print(l4)
# 	print "length: ", s.ll_len(l4)

# 	print "=== TEST ll_reverse ==="
# 	l5 = s.ll_reverse(l1)
# 	s.ll_print(l5)
# 	print "length: ", s.ll_len(l5)
# 	l6 = s.ll_reverse(l3)
# 	s.ll_print(l6)
# 	print "length: ", s.ll_len(l6)
# 	l7 = s.ll_reverse(l4)
# 	s.ll_print(l7)
# 	print "length: ", s.ll_len(l7)

# 	print "=== TEST addTwoNumbers ==="
# 	print "l1: "
# 	s.ll_print(l1)
# 	print "l2: "
# 	s.ll_print(l2)
# 	print ">>> "
# 	s.ll_print(s.addTwoNumbers(l1, l2))

# 	print "l1: "
# 	s.ll_print(l1)
# 	print "l8: "
# 	s.ll_print(l8)
# 	print ">>> "
# 	s.ll_print(s.addTwoNumbers(l1, l8))

# 	print "l1: "
# 	s.ll_print(l1)
# 	print "l9: "
# 	s.ll_print(l9)
# 	print ">>> "
# 	s.ll_print(s.addTwoNumbers(l1, l9))

# 	print "l9: "
# 	s.ll_print(l9)
# 	print "l10: "
# 	s.ll_print(l10)
# 	print ">>> "
# 	s.ll_print(s.addTwoNumbers(l9, l10))