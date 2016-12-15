/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode tmpHead = new ListNode(-1);

        tmpHead.next = head;

        ListNode tmpNode = tmpHead;

        while (tmpNode.next != null) {
            while (tmpNode.next.val == val) {
                tmpNode.next = tmpNode.next.next;

                if (tmpNode.next == null) {
                    return tmpHead.next;
                }
            }

            tmpNode = tmpNode.next;
        }

        return tmpHead.next;
    }
}
