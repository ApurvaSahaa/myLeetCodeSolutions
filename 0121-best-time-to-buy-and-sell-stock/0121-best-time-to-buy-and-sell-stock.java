class Solution {
    public int maxProfit(int[] prices) {
        int bestBuy = prices[0];
        int maxProfit = 0;
        
        for(int i = 1; i < prices.length; i++){
            int tempProfit = prices[i] - bestBuy;
            maxProfit = Math.max(tempProfit, maxProfit);
            bestBuy = Math.min(prices[i], bestBuy);
        }
        return maxProfit;
    }
}