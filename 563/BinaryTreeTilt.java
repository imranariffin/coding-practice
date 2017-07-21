import java.lang.Math;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}	

public class BinaryTreeTilt {
    public int findTilt(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return _findTilt(root) + findTilt(root.left) + findTilt(root.right);
    }
    
    private int _findTilt(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.abs(sum(root.left) - sum(root.right));
    }
    
    private int sum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return root.val + sum(root.left) + sum(root.right);
    }
}