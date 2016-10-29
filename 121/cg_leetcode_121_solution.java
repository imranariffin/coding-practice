public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        
        for (int i = 0; i < prices.length; i++) {
            if (i + 1 < prices.length && prices[i] >= prices[i + 1]) {
                continue;
            }
            
            int buy = prices[i];
            
            for (int j = i + 1; j < prices.length; j++) {
                int sell = prices[j];
                
                profit = Math.max(sell - buy, profit);
            }
        }
        
        return profit;
    }
}
