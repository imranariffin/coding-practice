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
        if (head == null || head != null && head.next == null) {
            return head;
        }
        
        ListNode ret = reverseList(head.next);
        
        head.next.next = head;
        head.next = null;  // Initialize to null, so lastNode.next points to null.
        
        return ret;
    }
}
