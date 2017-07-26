/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {

    int nlen;
    Random rand;
    ListNode head;

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        this.nlen = 0;
        this.rand = new Random();
        this.head = head;
        ListNode node = this.head;
        while (node != null) {
            this.nlen += 1;
            node = node.next;
        }
    }

    /** Returns a random node's value. */
    public int getRandom() {
        int c = rand.nextInt(nlen);
        ListNode node = this.head;
        while (c > 0) {
            node = node.next;
            c--;
        }
        return node.val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
