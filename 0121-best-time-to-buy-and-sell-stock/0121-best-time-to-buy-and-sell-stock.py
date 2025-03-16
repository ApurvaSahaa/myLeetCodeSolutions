class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l, r = 0, 1
        while l < r and r < len(prices):
            if prices[r] > prices[l]:
                maxp = max(maxp, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxp