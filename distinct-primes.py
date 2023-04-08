class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()

        for num in nums:
            curr = 2

            while curr * curr <= num:
                while num % curr == 0:
                    primes.add(curr)
                    num //= curr
                curr += 1

            if num >= curr:
                primes.add(num)

        return len(primes)
