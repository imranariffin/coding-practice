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
    public int sumOfLeftLeaves(TreeNode root) {
        return recurse(root, 0);
    }
    
    private int recurse(TreeNode node, int count) {
        if (node == null) {
            return count;
        }
        
        if (node.left != null) {
            if (node.left.left != null || node.left.right != null) {
                count += recurse(node.left, 0);
            }
            else
            {
                count += node.left.val;
            }
        }
        
        if (node.right != null) {
            if (node.right.left != null || node.right.right != null) {
                count += recurse(node.right, 0);
            }
        }
        
        return count;
    }
}
