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
	String ROOT = "root";
	String LEFT = "left";
	String RIGHT = "right";

	public int sumOfLeftLeaves(TreeNode root) {
		return __sumLeftLeaves__(root, ROOT);
	}

	private int __sumLeftLeaves__(TreeNode root, String type) {
		// traverse like normal
		if (root == null) 
			return 0;
		// if (type == ROOT && root.left == null && root.right == null)
		// 	return 0;

		if (type == LEFT && root.left == null && root.right == null)
			return root.val;

		// if found left leaf, add to sum
		int sum = 0;
		if (root.left != null)
			sum += __sumLeftLeaves__(root.left, LEFT);
		if (root.right != null)
			sum += __sumLeftLeaves__(root.right, RIGHT);

		return sum;
	}
}