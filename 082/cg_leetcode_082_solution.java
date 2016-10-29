/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode currNode = head;
        
        while (currNode != null) {
            if (currNode.next == null) {
                break;
            }
            
            ListNode nextNode = currNode.next;
            
            while (nextNode != null && currNode.val == nextNode.val) {
                nextNode = nextNode.next;
            }
            
            currNode.next = nextNode;
            currNode = nextNode;
        }
        
        return head;
    }
}
