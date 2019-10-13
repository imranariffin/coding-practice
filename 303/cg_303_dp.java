public class NumArray {
    int[] cumu = null;
    
    // Notice that sum[i][j] = sum[i][j - 1] + arr[j] is equivalent to
    // sum[i][j] = sum[0][j] - sum[0][i - 1] = cum[j] - cum[i - 1].
    // Instead of using sum[i][j] which will require 2D array for the DP,
    // we use 1D cumulation array (cum). We normalize 0-based to
    // 1-based index to handle the case where i - 1 when i = 0.
    public NumArray(int[] nums) {
        int n = nums.length;
        cumu = new int[n + 1];
        for (int i = 1; i <= n; ++i) {
            cumu[i] = nums[i - 1] + cumu[i - 1];
        }
    }
    
    // Normalize i and j to 1-based index and get the result from DP table.
    public int sumRange(int i, int j) {
        return cumu[++j] - cumu[++i - 1];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
