/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        
        int lenA = getLength(headA);
        int lenB = getLength(headB);
        int lenDiff = Math.abs(lenA - lenB);
        ListNode nodeA = lenA > lenB ? getNode(headA, lenDiff) : headA;
        ListNode nodeB = lenB > lenA ? getNode(headB, lenDiff) : headB;
        
        while (nodeA != null && nodeB != null) {
            if (nodeA.val == nodeB.val) {
                return nodeA;
            }
            
            nodeA = nodeA.next;
            nodeB = nodeB.next;
        }
        
        return null;
    }
    
    private int getLength(ListNode node) {
        if (node == null) {
            return 0;
        }
        
        int len = 0;
        ListNode tmp = node;
        
        while (tmp != null) {
            len++;
            tmp = tmp.next;
        }
        
        return len;
    }
    
    private ListNode getNode(ListNode node, int d) {
        ListNode tmp = node;
        
        for (int i = 0; i < d; i++) {
            tmp = tmp.next;
        }
        
        return tmp;
    }
}
