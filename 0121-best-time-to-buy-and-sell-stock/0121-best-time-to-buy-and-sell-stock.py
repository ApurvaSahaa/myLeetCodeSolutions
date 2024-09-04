class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # going forward in time - for loop
        # have a curr profit to maximize - start with 0
        # for first day profit is zero
        # for next day check if the curr price is greater than yesterdays price
        # store yesterdays price as min price
        # since curr price is greater profit becomes curr price minus min price
        # update profit as max of curr profit and max profit
        # if curr price is smaller than min price update min price
        
        
        maxprofit = 0
        minprice = prices[0]
        
        for i in prices:
            if i > minprice:
                currprofit = i - minprice
                maxprofit = max(maxprofit, currprofit)
            if i < minprice:
                minprice = i
                
        return maxprofit
                
            