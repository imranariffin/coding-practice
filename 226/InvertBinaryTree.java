
// Definition for a binary tree node.
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode(int x) { val = x; }
  TreeNode(int x, TreeNode _left, TreeNode _right) {
  	val = x; left = _left; right = _right;
  }
}

public class InvertBinaryTree {
  public static TreeNode invertTree(TreeNode root) {
  	_invert(root);
  	return root;
  }

  private static void _invert(TreeNode root) {
  	if (root == null) {return;}
  	TreeNode temp = root.left;
  	root.left = root.right;
  	root.right = temp;
  	_invert(root.left); _invert(root.right);
  }
}