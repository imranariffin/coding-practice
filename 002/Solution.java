/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		int len1 = LNLength(l1);
		int len2 = LNLength(l2);

		if (len1 < len2) {
			int temp = len1;
			len1 = len2;
			len2 = temp;
			ListNode tempLN = l1;
			l1 = l2;
			l2 = tempLN;
		}

		// create empty return listnode
		ListNode ret = new ListNode(0);
		ListNode node = ret;
		int i = 1;
		while (i < len1) {
			node.next = new ListNode(0);
			node = node.next;
			i++;
		}

		int s, c;
		c = 0; i = 0;
		ListNode n1, n2;
		node = ret; n1 = l1; n2 = l2;
		while (n1 != null) {
			if (i < len2) {
				node.val = (c + n1.val + n2.val)%10;
				System.out.format("(" + n1.val + " + " + n2.val + " + " + c + " => " + node.val + ")->");
				c = (c + n1.val + n2.val) > 9 ? 1:0;
			}
			else {
				node.val = (c + n1.val)%10;
				System.out.format("(" + n1.val + " + 0 " + c + " => " + node.val + ")->");
				c = (c + n1.val) > 9 ? 1:0;
			}

			if (node.next == null && c == 1)	node.next = new ListNode(c);
			else if (node != null) 						node = node.next;
			if (n1 != null) 									n1 = n1.next;
			if (n2 != null) 									n2 = n2.next;

			i++;
		}
		System.out.format("\n");

		return ret;
	}

	private void
	printLN(ListNode ll) {
		while (ll != null) {
			System.out.format(ll.val + "->");
			ll = ll.next;
		}
		System.out.format("\n");
	}

	private int 
	LNLength(ListNode ll) {
		int len = 0;
		while (ll != null) {
			ll = ll.next;
			len++;
		}
		return len;
	}

	public static void
	main(String[] args) {
		Solution s = new Solution();

		ListNode ll = new ListNode(1);
		ll.next = new ListNode(2);
		ll.next.next = new ListNode(3);
		ll.next.next.next = new ListNode(4);
		// ListNode ll = null;
		System.out.println(s.LNLength(ll));

		s.addTwoNumbers(null, ll);

		ListNode l1 = new ListNode(2);
		l1.next = new ListNode(4);
		l1.next.next = new ListNode(3);
		ListNode l2 = new ListNode(5);
		l2.next = new ListNode(6);
		l2.next.next = new ListNode(4);
		s.printLN(l1);
		s.printLN(l2);
		s.printLN(s.addTwoNumbers(l1, l2));

		return;
	}
}