public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        int n_1 = findNums.length;
        int n_2 = nums.length;

        int[] res = new int[n_1];

        for (int i = 0; i < res.length; ++i) {
            res[i] = -1;
        }

        for (int i = 0; i < n_1; ++i) {
            for (int j = 0; j < n_2; ++j) {
                if (nums[j] == findNums[i]) {
                    for (int k = j + 1; k < n_2; ++k) {
                        if (nums[k] > nums[j]) {
                            res[i] = nums[k];
                            break;
                        }
                    }

                    break;
                }
            }
        }

        return res;
    }
}
