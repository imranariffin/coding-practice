public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cc = 0;
        int cm = cc;
        for (int num : nums) {
            if (num == 0) {
                cc = 0;
            } else {
                cc += 1;
                cm = Math.max(cm, cc);
            }
        }
        return cm;
    }
}
