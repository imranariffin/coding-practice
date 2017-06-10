
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
 

class BinTree2Str {
	private static StringBuilder sb = new StringBuilder();
	
	public static String tree2str(TreeNode t) {
		_tree2str(t, true);
		String ret = sb.substring(1, sb.length()-1);
		sb = new StringBuilder();
		return ret;
	}

	private static void _tree2str(TreeNode t, boolean show) {
		if (t == null) { 
			if (show) {
				sb.append('(').append(')'); return; 
			}
			return;
		}

		sb.append('(').append(t.val);
		if (t.left == null && t.right == null) { 
			_tree2str(t.left, false); _tree2str(t.right, false); 
		}
		else if (t.left == null && t.right != null) { 
			_tree2str(t.left, true); _tree2str(t.right, true); 
		}
		else if (t.left != null && t.right == null) { 
			_tree2str(t.left, true); _tree2str(t.right, false); 
		}
		else { 
			_tree2str(t.left, true); _tree2str(t.right, true); 
		}
		sb.append(')');
	}

	public static void main(String[] args) {
		TreeNode t = new TreeNode(1,
			new TreeNode(2, 
				new TreeNode(4),
				null),
			new TreeNode(3));
		String ans = tree2str(t);
		System.out.println(ans);

		TreeNode t2 = new TreeNode(1,
			new TreeNode(2, 
				null,
				new TreeNode(4)),
			new TreeNode(3));
		ans = tree2str(t2);
		System.out.println(ans);

		TreeNode t3 = new TreeNode(1);
		ans = tree2str(t3);
		System.out.println(ans);

		TreeNode t4 = null;
		ans = tree2str(t4);
		System.out.println(ans);

		TreeNode t5 = new TreeNode(1, 
			new TreeNode(2), 
			new TreeNode(3));
		ans = tree2str(t5);
		System.out.println(ans);

		TreeNode t6 = new TreeNode(1, 
			null, 
			new TreeNode(3));
		ans = tree2str(t6);
		System.out.println(ans);
	}
}