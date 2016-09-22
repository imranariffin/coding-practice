import java.lang.Math;
import java.util.List;
import java.util.ArrayList;

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