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
        
        int lenA = 0;
        int lenB = 0;
        ListNode nodeA = headA;
        ListNode nodeB = headB;
        
        while (nodeA.next != null) {
            nodeA = nodeA.next;
            lenA++;
        }
        
        while (nodeB.next != null) {
            nodeB = nodeB.next;
            lenB++;
        }
        
        if (nodeA.val != nodeB.val) {
            return null;
        }
        
        int lenDiff = Math.abs(lenA - lenB);
        
        nodeA = headA;
        nodeB = headB;
        
        if (lenA > lenB) {
            for (int i = 0; i < lenDiff; i++) {
                nodeA = nodeA.next;
            }
        }
        
        if (lenB > lenA) {
            for (int i = 0; i < lenDiff; i++) {
                nodeB = nodeB.next;
            }
        }
        
        while (nodeA.val != nodeB.val) {
            nodeA = nodeA.next;
            nodeB = nodeB.next;
        }
        
        return nodeA;
    }
}
