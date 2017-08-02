public class Solution {
    public int longestPalindromeSubseq(String s) {
        List<Character> char_list = s.chars()
            .mapToObj(x -> (char) x)
            .collect(Collectors.toList());
        int n = char_list.size();

        int[][] dp = new int[n][n];
        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
        }

        for (int i = 1; i < n; ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (char_list.get(i) == char_list.get(j)) {
                    dp[j][i] = dp[j + 1][i - 1] + 2;
                } else {
                    dp[j][i] = Math.max(dp[j + 1][i], dp[j][i - 1]);
                }

                // System.out.printf("dp[%d, %d] = %d\n", j, i, dp[j][i]);
            }
        }

        return dp[0][n - 1];
    }
}
