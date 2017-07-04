import java.util.ArrayList;
import java.util.Arrays;
 
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) { return true; }
        return isSymmetricHelper(root.left, root.right);
    }

    private boolean isSymmetricHelper(TreeNode left, TreeNode right) {
        if (left == null || right == null) {
            return left == right;
        }

        if (left.val != right.val) {
            return false;
        }

        boolean ret = 
            isSymmetricHelper(left.left, right.right) &&
            isSymmetricHelper(left.right, right.left);
        return ret;
    }

    public static void
    main(String[] args) {
        Solution s = new Solution();

        // [1,2,2,3,4,4,3]
        TreeNode node = 
            new TreeNode(1, 
                new TreeNode(2, 
                    new TreeNode(3, null, null),
                    new TreeNode(4, null, null)),
                new TreeNode(2, 
                    new TreeNode(4, null, null),
                    new TreeNode(3, null, null)));
        System.out.println(s.isSymmetric(node));

        // [1,2,3,3,null,2,null]
        TreeNode node1 = 
            new TreeNode(1, 
                new TreeNode(2, 
                    new TreeNode(3),
                    null),
                new TreeNode(3, 
                    new TreeNode(2),
                    null));
        System.out.println(s.isSymmetric(node1));
    }
}