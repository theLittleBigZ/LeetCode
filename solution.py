class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for price in range(len(prices)-1):
            if(prices[price] < prices[price+1]):
                maxProfit += prices[price+1] - prices[price]
        return maxProfit
