/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.HashMap;

public class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        // memoize each node's height
        HashMap<TreeNode, Integer>
            hMap = new HashMap<TreeNode, Integer>();
        hMap.put(null, 0);
        height(root, hMap);
        
        return __isBalanced(root, hMap);
    }

    private boolean 
    __isBalanced(TreeNode node, HashMap<TreeNode, Integer> hMap) {
        if (node == null) {
            return true;
        }

        int hLeft = (int)hMap.get(node.left);
        int hRight = (int)hMap.get(node.right);

        if (abs(hLeft - hRight) > 1) {
            return false;
        }
        return 
            __isBalanced(node.left, hMap) &&
            __isBalanced(node.right, hMap);
    }

    private int
    height(TreeNode node, HashMap<TreeNode, Integer> hMap) {
        if (node == null) {
            return 0;
        }
        int h = 1 + max(height(node.left, hMap), height(node.right, hMap));
        hMap.put(node, h);
        return h;
    }
    
    private int
    abs(int n) {
        return n>0 ? n:-n;
    }

    private int
    max(int x, int y) {
        return x>y ? x:y;
    }
}