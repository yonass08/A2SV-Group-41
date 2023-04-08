class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        left = max(left, 2)
        primes = [True] * (right-left+1)

        i = 2
        while i*i <= right:
            start = max(((left + i - 1) // i), 2) * i
            for j in range(start, right+1, i):
                primes[j-left] = False
            i += 1

        res = [-1, -1]
        gap = right - left + 1
        prev = -1
        
        for i in range(len(primes)):
            if primes[i]:
                if prev >= 0 and i - prev < gap:
                    gap = i - prev
                    res = [left + prev, left + i]
                prev = i

        return res
