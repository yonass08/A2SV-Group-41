class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        isPrime = [1] * (n)
        isPrime[0] = isPrime[1] = 0
        
        i = 2
        res = n-2
        
        while i * i <= n:
            if isPrime[i] == 0:
                i += 1
                continue
                
            for num in range(i * i, n, i):
                if isPrime[num]:
                    res -= 1
                isPrime[num] = 0
                
            i += 1
                
        return res
