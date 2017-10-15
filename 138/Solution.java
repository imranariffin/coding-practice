/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    Map<RandomListNode,RandomListNode> copied = new HashMap<>();
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return null;
        }
        if (copied.containsKey(head)) {
            return copied.get(head);
        }
        
        RandomListNode node = new RandomListNode(head.label);
        copied.put(head, node);
        node.next = copyRandomList(head.next);
        node.random = copyRandomList(head.random);
        return node;
    }
}
