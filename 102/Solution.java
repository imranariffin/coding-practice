/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        return (new BinTreeLevelTraversal()).level_order(root);
    }

    public static void main(String[] args) {
    	Solution s = new Solution();
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
		System.out.println("TEST 1");
		System.out.println(s.levelOrder(t));
		System.out.println("TEST 2");
		t = new TreeNode(3, 
				new TreeNode(9, null, null),
				new TreeNode(20,
					new TreeNode(15, null, null),
					new TreeNode(7, null, null)));
		System.out.println(s.levelOrder(t));
    }

	public class BinTreeLevelTraversal {

		void get_level(TreeNode t, int i, int lvl, List<List<Integer>> ret) {
			assert i >= 0;
			assert t != null;
			assert ret != null;
			assert ret.get(i) != null;
			
			if (i >= lvl-1) {
				ret.get(i).add(t.val);
				return;
			}
			if (t.left != null) get_level(t.left, i+1, lvl, ret);
			if (t.right != null) get_level(t.right, i+1, lvl, ret);
		}

		int height(TreeNode t) {
			if (t == null) return 0;
			return 1+Math.max(height(t.left), height(t.right));
		}

		void __level_order__(TreeNode t, List<List<Integer>> ret) {
			int h = height(t);
			for (int i=0; i<h; i++) {
				ret.add(new ArrayList<Integer>());
				get_level(t, 0, i+1, ret);
			}
		}

		List<List<Integer>> level_order(TreeNode t) {
			List<List<Integer>> ret = new ArrayList<List<Integer>>();
			__level_order__(t, ret);
			return ret;
		}
	}
}