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
    public boolean hasPathSum(TreeNode root, int sum) {
        return root != null ? recurse(root, null, sum, 0) : false;
    }
    
    private boolean recurse(TreeNode node, TreeNode parent, int target, int sum) {
        if (node == null) {
            return (parent != null && parent.left == null && parent.right == null && sum == target) ? true : false;
        }
        
        return recurse(node.left, node, target, sum + node.val) || recurse(node.right, node, target, sum + node.val);
    }
}
