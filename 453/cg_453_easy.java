public class Solution {
    public int minMoves(int[] nums) {
        int move = 0;
        
        Arrays.sort(nums);
        
        for (int i = 1; i < nums.length; i++) {
            move += nums[i] - nums[0];
        }
        
        return move;
    }
}
