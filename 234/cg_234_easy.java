/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> l0 = new ArrayList<>();
        ListNode node = head;
        
        while (node != null) {
            l0.add(node.val);
            node = node.next;
        }
        
        List<Integer> l1 = new ArrayList<>(l0);
        
        Collections.reverse(l1);
        
        for (int i = 0; i < l0.size(); i++) {
            if (Integer.compare(l0.get(i), l1.get(i)) != 0) {
                return false;
            }
        }
        
        return true;
    }
}
