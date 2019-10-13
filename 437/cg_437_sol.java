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
    public int pathSum(TreeNode root, int sum) {
        if (root == null) {
            return 0;
        }
        
        ArrayDeque<TreeNode> D = new ArrayDeque<TreeNode>();
        int pathCount = 0;
        
        D.push(root);
        
        while (!D.isEmpty()) {
            TreeNode node = D.pop();
            
            pathCount += recurse(node, sum, 0);
            
            if (node.left != null) {
                D.push(node.left);
            }
            
            if (node.right != null) {
                D.push(node.right);
            }
        }
        
        return pathCount;
    }
    
    public int recurse(TreeNode node, int sum, int currSum) {
        if (node == null) {
            return 0;
        }
        
        currSum += node.val;
        
        if (currSum == sum) {
            return 1 + recurse(node.left, sum, currSum) + recurse(node.right, sum, currSum);
        }
        
        return recurse(node.left, sum, currSum) + recurse(node.right, sum, currSum);
    }
}
