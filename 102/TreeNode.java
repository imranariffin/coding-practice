public class TreeNode {
	public int val;
	public TreeNode left;
	public TreeNode right;

	public TreeNode(int x) {
		this.val = x;
		this.left = null;
		this.right = null;
	}

	public TreeNode(int x, TreeNode l, TreeNode r) {
		this.val = x;
		this.left = l;
		this.right = r;
	}
}