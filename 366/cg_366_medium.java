/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        
        travel(root, res);
        
        return res;
    }
    
    private int travel(TreeNode node, List<List<Integer>> res) {
        if (null == node) {
            return -1;
        }
        
        int level = Math.max(1 + travel(node.left, res), 1 + travel(node.right, res));
        
        while (res.size() - 1 < level) {
            res.add(new ArrayList<Integer>());
        }
        
        res.get(level).add(node.val);
        
        return level;
    }
}
