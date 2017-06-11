public class BestTimeStock {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;
        
        int n = prices.length;
        int ret = 0;
        int minPrice = Integer.MAX_VALUE;
        for (int i=0; i<n; i++) {
            minPrice = Integer.min(minPrice, prices[i]);
            ret = Integer.max(ret, prices[i] - minPrice);
        }
        return ret;
    }
}