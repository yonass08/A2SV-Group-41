class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(idx, buy):
            if idx >= len(prices):
                return 0
            
            if buy:
                return max(dp(idx+1, buy), dp(idx+1, not buy) - prices[idx])
            else:
                return max(dp(idx+1, buy), dp(idx+2, not buy) + prices[idx])
            
        return dp(0, True)
            
            