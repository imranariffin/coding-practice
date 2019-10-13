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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        Queue<CustomNode> queue = new LinkedList<>();
        queue.offer(new CustomNode(root, 0));

        while (!queue.isEmpty()) {
            CustomNode u = queue.poll();

            if (u.treeNode == null) {
                continue;
            }

            if (result.size() < u.row + 1) {
                result.add(Integer.MIN_VALUE);
            }

            result.set(u.row, u.treeNode.val > result.get(u.row) ? u.treeNode.val : result.get(u.row));

            for (TreeNode treeNode : new TreeNode[] { u.treeNode.left, u.treeNode.right }) {
                queue.offer(new CustomNode(treeNode, u.row + 1));
            }
        }

        return result;
    }

    public class CustomNode {
        TreeNode treeNode;
        Integer row;

        CustomNode(TreeNode treeNode, Integer row) {
            this.treeNode = treeNode;
            this.row = row;
        }
    }
}
