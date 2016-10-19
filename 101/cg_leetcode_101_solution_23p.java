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
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        return recurse(root.left, root.right);
    }
    
    private boolean recurse(TreeNode node1, TreeNode node2) {
        if (node1 == null || node2 == null) {
            return node1 == node2;
        }
        
        if (node1.val != node2.val) {
            return false;
        }
        
        return recurse(node1.left, node2.right) && recurse(node1.right, node2.left);
    }
}
