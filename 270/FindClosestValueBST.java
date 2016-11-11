/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class FindClosestValueBST {
	// 2ms
    public int closestValue(TreeNode root, double target) {
    	return __closestValue__(root, target);
    }

    int getMax(TreeNode root) {
    	assert root!=null;

    	while (root.right != null)
    		root = root.right;
    	return root.val;
    }

    int getMin(TreeNode root) {
    	assert root!=null;

    	while (root.left != null)
    		root = root.left;
    	return root.val;
    }

    // include parent Value
    public int __closestValue__(TreeNode root, double target) {
    	assert root!=null;

    	if (target <= (float)root.val) {
    		if (root.left != null) {
    			int leftmax = getMax(root.left);
    			if (target > (double) leftmax) {
    				// compare max node from left with current node
					double leftmaxdist = target - leftmax;
					double rootdist = root.val - target;
    				if (leftmaxdist < rootdist) {
    					return leftmax;
    				}
    				return root.val;
    			}
    			return __closestValue__(root.left, target);
    		}
    		return root.val;
    	}

    	else {
    		if (root.right != null) {
    			int rightmin = getMin(root.right);
    			if (target < (double) rightmin) {
    				double rightmindist = rightmin - target;
    				double rootdist = target - root.val;
    				if (rightmindist < rootdist) {
    					return rightmin;
    				}
    				return root.val;
    			}
    			return __closestValue__(root.right, target);
    		}
    		return root.val;
    	}
    }

    public static void main(String[] args) {
    	System.out.println("Hello World!");
    	return;
    }
}