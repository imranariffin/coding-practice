import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.stream.Collectors;


// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class FindDuplicateSubtrees {    
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> iterList = getTraversal(root);
        
        Map<TreeNode,String> ids = new HashMap<>();
        for (int i = 0; i < iterList.size(); i++) {
            // String id = iterList.subList(i, iterList.size())
            //     .stream().map(t -> toString(t)).collect(Collectors.joining(","));
            String id = getTraversal(iterList.get(i))
                .stream().map(t -> toString(t)).collect(Collectors.joining(","));
            TreeNode node = iterList.get(i);
            ids.put(node, id);
        }
        
        Map<String,List<TreeNode>> invIndex = new HashMap<>();
        for (TreeNode t: iterList) {
            if (t != null) {
                String id = ids.get(t);
                // System.out.println(String.valueOf(t) + ": " + id);
                if (invIndex.containsKey(id)) {
                    invIndex.get(id).add(t);
                } else {
                    List<TreeNode> val = new ArrayList<>();
                    val.add(t);
                    invIndex.put(id, val);
                }   
            }
        }
        
        List<TreeNode> ret = new ArrayList<>();
        for (String key: invIndex.keySet()) {
            // System.out.println(key + ": " + invIndex.get(key));
            if (invIndex.get(key).size() > 1) {
                ret.add(invIndex.get(key).get(0));
            }
        }
        
        return ret;
    }
    
    private String toString(TreeNode t) {
        if (t == null) {
            return "null";
        }
        return Integer.toString(t.val);
    }
    
    private List<TreeNode> getTraversal(TreeNode t) {
        List<TreeNode> iterList = new ArrayList<TreeNode>();
        traversePreOrder(t, iterList);
        return iterList;
    }
    
    private void traversePreOrder(TreeNode t, List<TreeNode> iterList) {
        iterList.add(t);
        if (t == null) {
            return;
        }
        traversePreOrder(t.left, iterList);
        traversePreOrder(t.right, iterList);
    }
}