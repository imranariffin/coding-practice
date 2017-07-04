/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.Deque;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<TreeNode>();
        HashSet<TreeNode> visited = new HashSet<TreeNode>();
        List<Integer> list = new ArrayList<Integer>();

        if (root == null) {
        	return list;
        }

        TreeNode node = root;
        stack.addFirst(node);

        while (true) {
        	if (node.left != null && !visited.contains(node)) {
        		node = node.left;
        		stack.addFirst(node);
        	} else {
        		node = stack.removeFirst();
        		visited.add(node);
        		list.add(node.val);

        		if (node.right != null) {
        			node = node.right;
        			stack.addFirst(node);
        		}
        	}

        	if (stack.size() == 0) {
        		break;
        	}
        }

        return list;
    }

    public static void main(String[] args) {
    	Solution s = new Solution();

    	System.out.println("TEST 0");
    	TreeNode t0 = new TreeNode(1,
    		new TreeNode(2,
    			new TreeNode(3),
    			null),
    		null);
    	System.out.println(s.inorderTraversal(t0));

    	System.out.println("TEST 1");
    	TreeNode t1 = new TreeNode(1,
    		null,
    		new TreeNode(2,
    			new TreeNode(3),
    			null));
    	System.out.println(s.inorderTraversal(t1));
    }
}