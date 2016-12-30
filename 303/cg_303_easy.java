public class NumArray {
    int[] nums;
    
    public NumArray(int[] nums) {
        this.nums = nums;
        
        for (int i = 1; i < this.nums.length; i++) {
            this.nums[i] += this.nums[i - 1];
        }
    }

    public int sumRange(int i, int j) {
        if (i < 1) {
            return nums[j];
        }
        
        return nums[j] - nums[i - 1];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
