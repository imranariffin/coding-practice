# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        anchor = ListNode(-1)
        anchor.next = head
        node = anchor

        while node != None:
          if node.next != None and node.next.val == val:
            node.next = node.next.next
            continue

          node = node.next

        return anchor.next
