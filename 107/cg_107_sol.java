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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        
        recurse(res, root, 0);
        Collections.reverse(res);
        
        return res;
    }
    
    private void recurse(List<List<Integer>> res, TreeNode node, int level) {
        if (node == null) {
            return;
        }
        
        while (res.size() - 1 < level) {
            res.add(new ArrayList<Integer>());
        }
        
        res.get(level).add(node.val);
        
        recurse(res, node.left, level + 1);
        recurse(res, node.right, level + 1);
        
        return;
    }
}
