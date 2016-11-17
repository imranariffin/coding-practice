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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        
        if (root != null) {
            travel(root, Integer.toString(root.val), res);
        }
        
        return res;
    }
    
    private void travel(TreeNode node, String s, List<String> res) {
        if (node.left == null && node.right == null) {
            res.add(s);
            
            return;
        }
        
        if (node.left != null) {
            travel(node.left, s + "->" + Integer.toString(node.left.val), res);
        }
        
        if (node.right != null) {
            travel(node.right, s + "->" + Integer.toString(node.right.val), res);
        }
    }
}
