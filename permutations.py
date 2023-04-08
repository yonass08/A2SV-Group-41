class Solution:
    def __init__(self):
        self.bitmap = 0

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack([], res, nums)
        return res
        

    def backtrack(self, curr, res, nums):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return

        for i in range(len(nums)):
            mask = 1 << i
            if mask & self.bitmap == 0:
                self.bitmap ^= mask
                curr.append(nums[i])
                self.backtrack(curr, res, nums)
                curr.pop()
                self.bitmap ^= mask
