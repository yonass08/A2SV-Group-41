class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, [], -1, res)

        return res

    def backtrack(self, nums, curr, last_index, res):
        res.append(curr)
        if last_index == len(nums)-1:
            return

        for i in range(last_index+1, len(nums)):
            self.backtrack(nums, curr + [nums[i]], i, res)
