/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(-1);
        ListNode node = head;
        
        while (l1 != null || l2 != null) {
            ListNode tmp = new ListNode(-1);
            
            node.next = tmp;
            node = tmp;
            
            if (l1 != null && l2 != null) {
                if (l1.val <= l2.val) {
                    node.val = l1.val;
                    l1 = l1.next;
                }
                else {
                    node.val = l2.val;
                    l2 = l2.next;
                }
            }
            else if (l1 == null) {
                node.val = l2.val;
                node.next = l2.next;
                
                break;
            }
            else {
                node.val = l1.val;
                node.next = l1.next;
                
                break;
            }
        }
        
        return head.next;
    }
}
