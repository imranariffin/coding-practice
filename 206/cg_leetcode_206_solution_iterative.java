/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode node = head;
        
        while (node != null) {
            ListNode tmp = node.next;
            
            node.next = prev;
            prev = node;
            node = tmp;
        }
        
        return prev;
    }
}
