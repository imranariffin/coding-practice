public class Solution {
    public void moveZeroes(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int p = i;
            
            while (p > 0 && nums[p] != 0 && nums[p - 1] == 0) {
                nums[p - 1] = nums[p];
                nums[p] = 0;
                p -= 1;
            }
        }
    }
}
