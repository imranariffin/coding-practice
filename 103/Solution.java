/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    	return zigzag_traverse(root);
    }

	public void 
	__zigzag_traverse__(TreeNode t, int lvl, boolean odd, List<List<Integer>>ret) {
		if (t == null) return;
		while (ret.size() <= lvl) ret.add(new ArrayList<Integer>());

		if (!odd) {
			// inorder
			if (t.left != null)
				__zigzag_traverse__(t.left, lvl+1, odd, ret);
			if (lvl%2 == 0)
				ret.get(lvl).add(t.val);
			if (t.right != null)
				__zigzag_traverse__(t.right, lvl+1, odd, ret);
		} else {
			// postorder
			if (t.right != null)
				__zigzag_traverse__(t.right, lvl+1, odd, ret);
			if (lvl%2 != 0)
				ret.get(lvl).add(t.val);
			if (t.left != null)
				__zigzag_traverse__(t.left, lvl+1, odd, ret);
		}
	}

    public List<List<Integer>> zigzag_traverse(TreeNode t) {
    	List<List<Integer>> ret = new ArrayList<List<Integer>>();
    	__zigzag_traverse__(t, 0, false, ret);
    	__zigzag_traverse__(t, 0, true, ret);
    	return ret;
    }

    public static void
    main(String[] args) {
		TreeNode
		t = new TreeNode(8, 
			new TreeNode(4, 
				new TreeNode(2, 
					new TreeNode(1, null, null),
					new TreeNode(3, null, null)),
				new TreeNode(6,
					new TreeNode(5, null, null),
					new TreeNode(7, null, null))),
			new TreeNode(12,
				new TreeNode(10,
					new TreeNode(9, null, null),
					new TreeNode(11, null, null)),
				new TreeNode(14,
					new TreeNode(13, null, null),
					new TreeNode(15, null, null))));
		Solution s = new Solution();
		System.out.println(s.zigzagLevelOrder(t));
    }
}