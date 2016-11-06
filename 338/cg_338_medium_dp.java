public class Solution {
    int[] dp = new int[16];
    
    public int[] countBits(int num) {
        for (int i = 0; i < dp.length; i++) {
            dp[i] = -1;
        }
        
        int[] res = new int[num + 1];
        
        for (int i = 0; i <= num; i++) {
            int x = i;
            
            res[i] = calculateFast(x);
        }
        
        return res;
    }
    
    private int calculate(int x) {
        int count = 0;
        
        while (x != 0) {
            count += x & 1;
            x = x >>> 1;
        }
        
        return count;
    }
    
    private int calculateFast(int x) {
        int count = 0;
        
        while (x != 0) {
            if (dp[x & 15] == -1) {
                dp[x & 15] = calculate(x & 15);
            }
            
            count += dp[x & 15];
            x = x >>> 4;
        }
        
        return count;
    }
}
