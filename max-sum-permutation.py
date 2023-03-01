class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ind = [0] * (len(nums) + 1)

        for start, end in requests:
            ind[start] += 1
            ind[end+1] -= 1

        ind.pop()
        for i in range(1, len(ind)):
            ind[i] += ind[i-1]

        ind.sort()
        nums.sort()

        res = 0
        for i in range(len(nums)):
            res = (res + nums[i]*ind[i]) % (10**9+7)

        return res
