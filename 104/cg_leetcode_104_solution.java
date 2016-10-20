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
    public int maxDepth(TreeNode root) {
        return recurse(root, 0);
    }
    
    private int recurse(TreeNode node, int d) {
        if (node == null) {
            return d;
        }
        
        return max(recurse(node.left, d + 1), recurse(node.right, d + 1));
    }
    
    private int max(int a, int b) {
        return (a >= b) ? a : b;
    }
}
