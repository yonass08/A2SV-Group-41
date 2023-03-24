class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            self.backtrack([], i, nums, res)

        return [list(x) for x in res]


    def backtrack(self, curr, cand, nums, res):
        curr.append(nums[cand])

        if len(curr) >= 2:
            res.add(tuple(curr))

        for i in range(cand+1, len(nums)):
            if curr == [] or nums[i] >= curr[-1]:
                self.backtrack(curr, i, nums, res)

        curr.pop()
