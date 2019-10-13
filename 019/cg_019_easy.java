/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummyHead = new ListNode(-1);
        
        dummyHead.next = head;
        recurse(dummyHead, head, n);
        
        return dummyHead.next;
    }
    
    private int recurse(ListNode prev, ListNode node, int n) {
        if (node == null) {
            return 1;
        }
        
        int ret = recurse(node, node.next, n);
        
        if (ret == n) {
            prev.next = node.next;
        }
        
        return 1 + ret;
    }
}
