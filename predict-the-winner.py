class Solution:
    def __init__(self):
        self.memo = {}

    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.max_difference(nums, 0, len(nums) - 1) >= 0
        

    def max_difference(self, nums, start, end):
        if start == end:
            return nums[start]
        
        if end - start == 1:
            return max(nums[start], nums[end]) - min(nums[start], nums[end])

        if (start, end) in self.memo:
            return self.memo[(start, end)]

        # if i chose the first element the second player has two options

        # option 1 chose the first element
        op1 = nums[start + 1] - self.max_difference(nums, start + 2, end)

        # option 2 chose the last element
        op2 = nums[end] - self.max_difference(nums, start + 1, end - 1)

        # he will chose the best one
        choose_first = nums[start] -  max(op1, op2)


        # if i chose the last element the second player has two options

        # option 1 chose the first element
        op1 = nums[start] - self.max_difference(nums, start + 1, end - 1)

        # option 2 chose the last element
        op2 = nums[end - 1] - self.max_difference(nums, start, end - 2)

        # he will chose the best one
        choose_last = nums[end] -  max(op1, op2)

        res =  max(choose_first, choose_last)
        self.memo[(start, end)] = res
        return res
