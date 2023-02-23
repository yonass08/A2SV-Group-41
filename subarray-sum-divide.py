class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixes = [0] * k
        prefixes[0] = 1
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum = (curr_sum + num) % k
            res += prefixes[curr_sum]
            prefixes[curr_sum] += 1

        return res
