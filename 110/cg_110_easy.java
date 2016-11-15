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
    boolean b = true;
    
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        recurse(root, 1);
        
        return b;
    }
    
    private int recurse(TreeNode node, int level) {
        if (node == null) {
            return level;
        }
        
        int leftHeight = recurse(node.left, level + 1);
        int rightHeight = recurse(node.right, level + 1);
        
        if (Math.abs(leftHeight - rightHeight) > 1) {
            b = false;
        }
        
        return Math.max(leftHeight, rightHeight);
    }
}
