public class Solution {
    public int removeElement(int[] nums, int val) {
        int p0 = -1;
        int p1 = 0;
        
        while (p1 < nums.length) {
            if (nums[p1] == val) {
                p1++;
                
                continue;
            }
            
            nums[++p0] = nums[p1++];
        }
        
        return p0 + 1;
    }
}
