import java.util.List;
import java.util.Iterator;

public class Test {
	public static void main(String[] args) {
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

		BinTreeLevelTraversal 
		btlt = new BinTreeLevelTraversal();
		// btlt.inorder(t, 0, 2);

		// List<List<Integer>> ret = btlt.level_order(t);
		// for (Iterator it = ret.iterator(); it.hasNext();) {
		// 	List<Integer> ls = it.next();
		// 	for (Iterator itt = ls.iterator(); itt.hasNext();) {
		// 		Integer i = itt.next();
		// 		System.out.println(i);
		// 	}
		// }

		System.out.println("TEST 1");
		System.out.println(btlt.level_order(t));
		System.out.println("TEST 2");
		t = new TreeNode(3, 
				new TreeNode(9, null, null),
				new TreeNode(20,
					new TreeNode(15, null, null),
					new TreeNode(7, null, null)));
		System.out.println(btlt.level_order(t));
	}
}