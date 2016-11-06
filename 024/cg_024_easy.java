/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        pairSwap(head);
        
        return head;
    }
    
    private void pairSwap(ListNode node) {
        if (node == null || node.next == null) {
            return;
        }
        
        int tmp = node.val;
        
        node.val = node.next.val;
        node.next.val = tmp;
        
        pairSwap(node.next.next);
        
        return;
    }
}
