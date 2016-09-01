# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB

        # compare sizes
        sizeA = self.get_size(pA)
        sizeB = self.get_size(pB)
        diff = abs(sizeA - sizeB)

        # traverse bigger list until equal
        p = pA
        if sizeB > sizeA:
        	p = pB
        while diff != 0:
        	p = p.next
        	diff -= 1
        if sizeB > sizeA:
        	pB = p
        else:
        	pA = p
        assert(self.get_size(p) == self.get_size(pA) or self.get_size(p) == self.get_size(pB))        

        if pA == None or pB == None:
        	return None

        print "nA: ", pA.val, "@ ", id(pA)
        print "nB: ", pB.val, "@ ", id(pB)

        # traverse in parallel
        while pA != None and pB != None:

        	if pA is pB:
        		return pA

        	pA = pA.next
        	pB = pB.next

        return None

    def get_size(self, ll_head):
    	node = ll_head
    	size = 0
    	while node != None:
    		size += 1
    		node = node.next
    	return size