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
    public int minDepth(TreeNode root) {
        return root != null ? recurse(root, 1) : 0;
    }
    
    private int recurse(TreeNode node, int depth) {
        if (node.left == null && node.right == null) {
            return depth;
        }
        
        return Math.min(
            node.left != null ? recurse(node.left, depth + 1) : Integer.MAX_VALUE,
            node.right != null ? recurse(node.right, depth + 1) : Integer.MAX_VALUE
        );
    }
}
