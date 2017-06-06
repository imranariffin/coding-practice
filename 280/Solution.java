public class Solution {
    public static void wiggleSort(int[] nums) {
        if (nums == null || nums.length == 0 || nums.length == 1) 
            return;

        int n = nums.length;
        for (int i=0; i<n-1; i++) {
            int a = nums[i], b = nums[i+1];
            if (i%2==0) {
                if (a > b)
                    swap(nums, i, i+1);
            }
            else {
                if (a < b)
                    swap(nums, i, i+1);
            }
        }
    }
    
    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}