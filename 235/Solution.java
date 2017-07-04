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
import java.util.Arrays;

public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        ArrayList<TreeNode> pathP = 
        	new ArrayList<TreeNode>();
        ArrayList<TreeNode> pathQ = 
        	new ArrayList<TreeNode>();

        getPath(root, p, pathP);
        getPath(root, q, pathQ);

        System.out.println(Arrays.toString(pathP.toArray()));
        System.out.println(Arrays.toString(pathQ.toArray()));

        int lenP = pathP.size();
        int lenQ = pathQ.size();
        int len = lenP<lenQ? lenP:lenQ;

        for (int i = 0; i < len; i++) {
        	TreeNode pNode = pathP.get(i);
        	TreeNode qNode = pathQ.get(i);

        	if (pNode.val != qNode.val) {
        		return pathP.get(i-1);
        	}
        }
        return pathP.get(len-1);
    }

    private void
    getPath(TreeNode node, TreeNode target, ArrayList<TreeNode> path) {
    	if (node == null) {
    		return;
    	}
    	path.add(node);
    	if (node.val == target.val) {
    		return;
    	}

    	if (node.left != null && target.val < node.val) {
    		getPath(node.left, target, path);
    	} else {
    		getPath(node.right, target, path);
    	}
    }

    public static void main(String[] args) {
    	Solution s = new Solution();

    	System.out.println("TEST 0");
    	TreeNode node0 = new TreeNode(6,
    		new TreeNode(2, 
    			new TreeNode(0,
    				null,
    				null),
    			new TreeNode(4,
    				new TreeNode(3,
    					null,
    					null),
    				new TreeNode(5,
    					null,
    					null))),
    		new TreeNode(8,
    			new TreeNode(7,
    				null,
    				null),
    			new TreeNode(9,
    				null,
    				null)));
    	TreeNode p = new TreeNode(2);
    	TreeNode q = new TreeNode(4);
    	System.out.println(p.val + ", " + q.val);
    	System.out.println(">>> " + s.lowestCommonAncestor(node0, p, q));

   	System.out.println("TEST 1");
    	TreeNode node1 = new TreeNode(6,
    		new TreeNode(2, 
    			new TreeNode(0,
    				null,
    				null),
    			new TreeNode(4,
    				new TreeNode(3,
    					null,
    					null),
    				new TreeNode(5,
    					null,
    					null))),
    		new TreeNode(8,
    			new TreeNode(7,
    				null,
    				null),
    			new TreeNode(9,
    				null,
    				null)));
    	p = new TreeNode(2);
    	q = new TreeNode(8);
    	System.out.println(p.val + ", " + q.val);
    	System.out.println(">>> " + s.lowestCommonAncestor(node1, p, q));

   	System.out.println("TEST 2");
    	TreeNode node2 = new TreeNode(6,
    		new TreeNode(2, 
    			new TreeNode(0,
    				null,
    				null),
    			new TreeNode(4,
    				new TreeNode(3,
    					null,
    					null),
    				new TreeNode(5,
    					null,
    					null))),
    		new TreeNode(8,
    			new TreeNode(7,
    				null,
    				null),
    			new TreeNode(9,
    				null,
    				null)));
    	p = new TreeNode(7);
    	q = new TreeNode(0);
    	System.out.println(p.val + ", " + q.val);
    	System.out.println(">>> " + s.lowestCommonAncestor(node2, p, q));

   	System.out.println("TEST 3");
    	TreeNode node3 = new TreeNode(6,
    		new TreeNode(2, 
    			new TreeNode(0,
    				null,
    				null),
    			new TreeNode(4,
    				new TreeNode(3,
    					null,
    					null),
    				new TreeNode(5,
    					null,
    					null))),
    		new TreeNode(8,
    			new TreeNode(7,
    				null,
    				null),
    			new TreeNode(9,
    				null,
    				null)));
    	p = new TreeNode(0);
    	q = new TreeNode(5);
    	System.out.println(p.val + ", " + q.val);
    	System.out.println(">>> " + s.lowestCommonAncestor(node1, p, q));
    }
}