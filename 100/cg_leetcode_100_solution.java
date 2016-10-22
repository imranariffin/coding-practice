/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        ArrayDeque<TreeNode> P = new ArrayDeque<TreeNode>();
        ArrayDeque<TreeNode> Q = new ArrayDeque<TreeNode>();
        
        if (p == null && q == null) {
            return true;
        }
        
        if (p != null) {
            P.addFirst(p);
        }
        
        if (q != null) {
            Q.addFirst(q);
        }
        
        while (P.peekFirst() != null && Q.peekFirst() != null) {
            TreeNode currP = null;
            TreeNode currQ = null;
            
            if (P.peekFirst() != null) {
                currP = P.removeFirst();
            }
            
            if (Q.peekFirst() != null) {
                currQ = Q.removeFirst();
            }
            
            if (currP == null || currQ == null || currP.val != currQ.val) {
                return false;
            }
            
            if (currP.left != null && currQ.left != null) {
                P.addFirst(currP.left);
                Q.addFirst(currQ.left);
            }
            else if (currP.left == null && currQ.left == null) {
            }
            else {
                return false;
            }
            
            if (currP.right != null && currQ.right != null) {
                P.addFirst(currP.right);
                Q.addFirst(currQ.right);
            }
            else if (currP.right == null && currQ.right == null) {
            }
            else {
                return false;
            }
        }
        
        if (P.peekFirst() == null && Q.peekFirst() == null) {
            return true;
        }
        
        return false;
    }
}
