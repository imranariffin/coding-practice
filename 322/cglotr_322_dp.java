public class Solution {
    public int coinChange(int[] coins, int amount) {
        int MAX_N = amount + 1;
        int[] dp = new int[MAX_N];
        
        // MAX_N means no solution.
        for (int i = 0; i < MAX_N; ++i) {
            dp[i] = MAX_N;
        }
        
        dp[0] = 0;
        
        for (int i = 1; i < MAX_N; ++i) {
            for (int coin : coins) {
                
                // Of course coin > amount is impossible to satisfy.
                // If coin <= amount then the optimal solution is 1 + dp[amount - 1].
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
                }
            }
        }
        
        return dp[amount] < MAX_N ? dp[amount] : -1;
    }
}
