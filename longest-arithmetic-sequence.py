class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        res = 0
        diff = max(nums) - min(nums)
        step = 0
        
        while step * res <= diff:
            res = max(res, 
                    self.longestArthWithK(step, nums), 
                    self.longestArthWithK(-step, nums))
            step += 1

        return res

    def longestArthWithK(self, k, nums):
        bef = defaultdict(int)
        res = 0

        for num in nums:
            bef[num] = 1 + bef[num - k]
            res = max(res, bef[num])

        return res

        