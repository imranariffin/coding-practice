public class Solution {
    /*
    
    Invariant:
    1. Elements before slow pointers != 0.
    2. Elements in range [slow,fast) == 0.
    
    */
    public void moveZeroes(int[] nums) {
        int slow = 0;
        
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0) {
                int tmp = nums[slow];
                
                nums[slow++] = nums[fast];
                nums[fast] = tmp;
            }
        }
    }
}
