class Solution {
    public int maxProfit(int[] prices) {
        
        //pseudocode
        // we are given an integer array containing prices on each day
        // buy low sell high
        // we start buying on the first day so prices[0]
        // we declare a max profit variable
        // declare two pointers
            // one starting on the first day so prices[0]
            // second one starting on the next day so prices[1]
        // start iterating over the days
            // as long as the price keeps decreasing compared to the initial buy price keep moving 
            // right pointer ahead and changing left pointer to that day
            // (we are looking for a lower buy price so no matter ho high the corresponding elements are
            // we will always get the highest profit from the latest low buy price left pointer)
            
            // if the price increases for the right pointer subtract the left pointer price from the 
            // right pointer price
            // if it is more than the max profit vairable go ahead and update it
            
            // always maintain the left pointer less than or equal to right pointer
        
            // end when right pointer reaches length of the array
        
        int left  = 0;
        int right = left + 1;
        int maxProfit = 0;
        
        if (prices.length == 0 || prices.length == 1) return 0;
        
        while (left <= right && right < prices.length)
        {
            if (prices[right] > prices[left])
            {
                maxProfit = Integer.max(maxProfit, prices[right] - prices[left]);
                right ++;
            }
            else 
            {
                left = right;
                right ++;
            }
        }
        
        return maxProfit;
        
    }
}