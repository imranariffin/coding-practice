public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, List<Integer>> m = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (!m.containsKey(nums[i])) {
                m.put(nums[i], new ArrayList<Integer>());
            }
            
            List<Integer> indices = m.get(nums[i]);
            
            indices.add(i);
            
            if (indices.size() > 1 && indices.get(indices.size() - 1) - indices.get(indices.size() - 2) <= k) {
                return true;
            }
        }
        
        return false;
    }
}
