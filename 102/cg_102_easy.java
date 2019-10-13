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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        
        recurse(root, -1, res);
        
        return res;
    }
    
    private void recurse(TreeNode node, int level, List<List<Integer>> res) {
        if (node == null) {
            return;
        }
        
        level += 1;
        
        while (res.size() <= level) {
            res.add(new ArrayList<Integer>());
        }
        
        res.get(level).add(node.val);
        
        recurse(node.left, level, res);
        recurse(node.right, level, res);
    }
}
