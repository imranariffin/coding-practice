/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void deleteNode(ListNode node) {
        if (node == null) {
            return;
        }
        
        if (node.next == null) {
        }
        else if (node.next.next == null) {
            int tmp = node.next.val;
            
            node.next.val = node.val;
            node.val = tmp;
            node.next = null;
        }
        else {
            int tmp = node.next.val;
            
            node.next.val = node.val;
            node.val = tmp;
            
            deleteNode(node.next);
        }
    }
}
