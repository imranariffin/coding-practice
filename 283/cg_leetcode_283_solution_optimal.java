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
                swap(nums, slow++, fast);
            }
        }
    }

    private void swap(int[] arr, int p0, int p1) {
        int tmp = arr[p0];

        arr[p0] = arr[p1];
        arr[p1] = tmp;
    }
}
