public class FourKeysKeyboard {
    public int maxA(int N) {
        int[] dp = new int[N + 1];
        
        for (int i = 1; i <= N; i++) {
            dp[i] = i;
            for (int j = i - 3; j >= 1; j--) {
                dp[i] = Math.max(dp[i], dp[j] * (i - j - 1));
            }
        }
        return dp[N];
    }
}