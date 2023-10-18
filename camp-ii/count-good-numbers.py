class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens = n // 2 + n % 2
        odds = n // 2
        mod = 10 ** 9 + 7
        
        return (pow(5, evens, mod) * pow(4, odds, mod)) % mod
        