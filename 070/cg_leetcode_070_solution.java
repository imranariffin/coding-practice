public class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        
        Arrays.fill(dp, -1);
        
        return recurse(dp, n);
    }
    
    private int recurse(int[] dp, int n) {
        if (n < 0) {
            return 0;
        }
        
        if (dp[n] != -1) {
            return dp[n];
        }
        
        if (n == 0) {
            return 1;
        }
        
        int ret = recurse(dp, n - 1) + recurse(dp, n - 2);
        
        dp[n] = ret;
        
        return ret;
    }
}
