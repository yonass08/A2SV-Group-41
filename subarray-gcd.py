class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        res = 0

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i, len(nums)):
                curr = gcd(curr, nums[j])
                if curr % k != 0:
                    break
                if curr == k:
                    res += 1

        return res

