import java.util.Arrays;

public class Solution {
    public void wiggleSort(int[] nums) {
        int j; int N = nums.length;
        for (int i=0; i<N; i++) {
            if (i%2==0) {
                // System.out.println(Arrays.toString(nums));
                swap(nums, i, min(nums, i));
                // System.out.println(Arrays.toString(nums));
            }
            else {
                // System.out.println(Arrays.toString(nums));
                swap(nums, i, max(nums, i));
                // System.out.println(Arrays.toString(nums));
            }
            // System.out.println("---");
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    private int min(int[] nums, int i) {
        int btm = i;
        int N = nums.length;
        for (; i<N; i++) {
            if (nums[i] < nums[btm])
                btm = i;
        }
        return btm;
    }
    
    private int max(int[] nums, int i) {
        int top = i;
        int N = nums.length;
        for (; i<N; i++) {
            if (nums[i] > nums[top])
                top = i;
        }
        return top;
    }
}