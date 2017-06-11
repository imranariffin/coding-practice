
// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
    TreeNode(int x, TreeNode l, TreeNode r) { 
    	val = x; left = l; right = r;
    }
}

public class MergeBinTree {
	public static TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
		if (t1 == null && t2 == null) { return null; }
		
		TreeNode node = null;
		if (t1 == null ) { 
			node = new TreeNode(t2.val);
			node.left = mergeTrees(null, t2.left);
			node.right = mergeTrees(null, t2.right);
		} else if (t2 == null ) { 
			node = new TreeNode(t1.val);
			node.left = mergeTrees(t1.left, null);
			node.right = mergeTrees(t1.right, null);
		} else {
			node = new TreeNode(t1.val + t2.val);
			node.left = mergeTrees(t1.left, t2.left);
			node.right = mergeTrees(t1.right, t2.right);
		}
		return node;
	}

	// public static void main(String[] args) {
	// 	TreeNode p = new TreeNode(1,
	// 		new TreeNode(3,
	// 			new TreeNode(5),
	// 			null),
	// 		new TreeNode(2));

	// 	TreeNode q = new TreeNode(2,
	// 		new TreeNode(1,
	// 			null,
	// 			new TreeNode(4)),
	// 		new TreeNode(3,
	// 			null,
	// 			new TreeNode(7)));
	// }
}