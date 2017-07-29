public class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        if (m < 1) return 0;
        int n = matrix[0].length;
        if (n < 1) return 0;
        int[][] dp = new int[m][n];
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == '0') {
                    dp[i][j] = 0;
                    continue;
                }
                if (i == 0 || j == 0) {
                    dp[i][j] = matrix[i][j] - '0';
                } else {
                    dp[i][j] = Math.min(Math.min(dp[i][j - 1], dp[i - 1][j - 1]), dp[i - 1][j]) + 1;
                }
                // System.out.printf("(%d,%d) -> %d\n", i, j, dp[i][j]);
                res = Math.max(res, dp[i][j]);
            }
        }
        return res * res;
    }
}
