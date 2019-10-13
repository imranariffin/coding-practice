public class Solution {
    public int findLHS(int[] nums) {
        Arrays.sort(nums);

        int p_1 = 0;
        int p_2 = 0;
        int res = 0;

        while (p_2 < nums.length) {
            while (nums[p_2] - nums[p_1] > 1) {
                ++p_1;
            }

            res = Math.max(res, (nums[p_2] - nums[p_1] == 1) ? (p_2 - p_1 + 1) : 0);

            ++p_2;
        }

        return res;
    }
}
