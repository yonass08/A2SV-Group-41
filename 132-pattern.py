class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second_num = float('-inf')

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < second_num:
                    return True

            while stack and nums[i] > stack[-1]:
                second_num = stack.pop()

            stack.append(nums[i])

        return False
