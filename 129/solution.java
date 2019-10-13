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
    public int sumNumbers(TreeNode root) {
        Stack<Integer> st = new Stack<>();
        List<Integer> res = new LinkedList<>();
        dfsVisit(root, st, res);
        int sum = 0;
        for (int n : res) {
            sum += n;
        }
        return sum;
    }
    
    private void dfsVisit(TreeNode root, Stack<Integer> st, List<Integer> res) {
        if (root == null) {
            return;
        }
        st.push(root.val);
        if (root.left == null && root.right == null) {
            res.add(getRootToLeafNumber(st));
        } else {
            dfsVisit(root.left, st, res);
            dfsVisit(root.right, st, res);
        }
        st.pop();
    }
    
    private Integer getRootToLeafNumber(Stack<Integer> st) {
        StringBuilder sb = new StringBuilder();
        ListIterator<Integer> it = st.listIterator(0);
        while (it.hasNext()) {
            sb.append(it.next());
        }
        if (sb.toString().isEmpty()) {
            sb.append("0");
        }
        return Integer.valueOf(sb.toString());
    }
}
