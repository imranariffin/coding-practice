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
        if (head == null) {
            return head;
        }

        ListNode odd_head = head;
        ListNode odd_tail = odd_head;

        ListNode even_head = head.next;
        ListNode even_tail = even_head;

        while (even_tail != null && even_tail.next != null) {
            odd_tail.next = even_tail.next;
            odd_tail = odd_tail.next;

            even_tail.next = even_tail.next.next;
            even_tail = even_tail.next;
        }

        odd_tail.next = even_head;

        return head;
    }
}
