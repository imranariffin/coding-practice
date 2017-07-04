
// Definition for singly-linked list.
class ListNode {
	int val;
	ListNode next;
	ListNode(int x) {
		val = x;
		next = null;
	}
}

public class IntersectTwoLList {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    	int lenA = getLength(headA);
    	int lenB = getLength(headB);
    	ListNode pA = headA;
    	ListNode pB = headB;

    	// definitely no intersection
    	if (lenA == 0 || lenB == 0)
    		return null;

    	// start at same distance from interection
    	if (lenA < lenB) while (lenA < lenB) {pB = pB.next; lenB--;}
    	if (lenA > lenB) while (lenA > lenB) {pA = pA.next; lenA--;}

    	// move both pointers until match
    	while (lenA > 0) {
    		if (pA == pB)
    			return pA;
    		pA = pA.next;
    		pB = pB.next;
    		lenA--;
    		lenB--;
    	}
    	// no intersection
    	return null;
    }

    private int getLength(ListNode node) {
    	int len = 0;
    	while (node != null) {
    		len++;
    		node = node.next;
    	}
    	return len;
    }

    public static void main(String args[]) {
    	System.out.println("Hello World!");
    }
}