class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x

        return self.power(x, n)

    def power(self, x, n):
        if n == 0:
            return 1
    
        temp = self.power(x, n // 2)
        mul = x if n % 2 == 1 else 1

        return temp * temp * mul
