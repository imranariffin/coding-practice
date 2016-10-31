public class Solution {
    public int arrangeCoins(int n) {
        int rCoin = 1;
        int hCoin = 0;
        
        while (rCoin <= n) {
            n -= rCoin;
            rCoin += 1;
            hCoin += 1;
        }
        
        return hCoin;
    }
}
