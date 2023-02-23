class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        curr_sum = 0

        for num in nums:
            curr_sum += num
            res.append(curr_sum)

        return res
