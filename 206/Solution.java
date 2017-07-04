// 0 ms 36.62%
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
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode prev = head;
        ListNode cur = head.next;
        ListNode temp = null;
        head.next = null;
        
        while (cur != null) {
            temp = prev;
            prev = cur;
            cur = cur.next;
            prev.next = temp;
        }
        
        return prev;
    }
}