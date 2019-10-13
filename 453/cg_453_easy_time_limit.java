public class Solution {
    public int minMoves(int[] nums) {
        int move = 0;
        
        while (!isEqual(nums)) {
            move += increment(nums);
        }
        
        return move;
    }
    
    private boolean isEqual(int[] nums) {
        int val = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != val) {
                return false;
            }
        }
        
        return true;
    }
    
    private int increment(int[] nums) {
        Arrays.sort(nums);
        
        int move = nums[nums.length - 1] - nums[nums.length - 2];
        
        move = move != 0 ? move : 1;
        
        for (int i = 0; i < nums.length - 1; i++) {
            nums[i] += move;
        }
        
        return move;
    }
}
