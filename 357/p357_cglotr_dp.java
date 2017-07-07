public class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        if (n < 1) return 1;
        int[] dp = new int[11];
        dp[0] = 0;
        dp[1] = 10;
        for (int i = 2; i <= 10; ++i) {
            int count = 9;
            int x = 9;
            for (int j = 1; j < i; ++j) {
                count *= x--;
            }
            
            // The recurrence formula. Explanation:
            // 
            // n = 0 -> 0
            // n = 1 -> 10 [0 1 2 .. 9]
            // n = 2 -> dp[1] + count
            // 
            //          count = 9 * 9
            //                  i   j
            //          i since 9 digits to choose from
            //          j since 9 digits to choose from [0 .. 9] - {digit j}
            // 
            // n = 3 -> dp[2] + count
            // 
            //          count = 9 * 9 * 8
            //                  i   j   k
            //          k since [0 .. 9] - {i, j}
            // 
            // n = 3 -> ..
            dp[i] = dp[i - 1] + count;
        }
        return n < 11 ? dp[n] : dp[10];
    }
}
