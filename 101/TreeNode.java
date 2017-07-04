// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { 
    	val = x; 
    	this.left = null;
    	this.right = null;
    }
    TreeNode(int x, TreeNode left, TreeNode right) { 
        this.val = x; 
        this.left = left;
        this.right = right;
    }

    public String toString() {
    	return Integer.toString(val);
    }
}