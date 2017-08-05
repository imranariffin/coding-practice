/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return head;

        ListNode even_tail = new ListNode(-1);
        ListNode even_head = even_tail;

        ListNode node = head;
        while (node.next != null && node.next.next != null) {
            even_tail.next = node.next;
            even_tail = even_tail.next;
            node.next = node.next.next;
            even_tail.next = null;
            node = node.next;
        }

        if (node.next != null) {
            even_tail.next = node.next;
            even_tail = even_tail.next;
            even_tail.next = null;
        }

        node.next = even_head.next;

        return head;
    }
}
