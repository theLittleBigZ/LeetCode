class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][1] -= prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]
        return max(dp[-1])
