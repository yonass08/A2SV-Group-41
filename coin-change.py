class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {coin: 1 for coin in coins}
        memo[0] = 0

        res = self.helper(coins, amount, memo)
        return res if res < float('inf') else -1

    
    def helper(self, coins, amount, memo):
        if amount < 0 or 0 < amount < coins[0]:
            return float('inf')

        if amount not in memo:
            res = float('inf')
            for coin in coins:
                res = min(res, self.helper(coins, amount - coin, memo))
            memo[amount] = res + 1

        return memo[amount]

