public class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> S = new HashSet<Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            if (S.contains(nums[i])) {
                return true;
            }
            
            S.add(nums[i]);
        }
        
        return false;
    }
}
