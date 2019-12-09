class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLen(headA)
        lenB = self.getLen(headB)

        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while headA != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getLen(self, head):
        n = 0
        while head != None:
            head = head.next
            n += 1
        return n

