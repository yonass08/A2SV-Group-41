class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        num_less = 0
        num_equal = 0 

        for num in nums:
            if num < pivot:
                num_less += 1
            elif num == pivot:
                num_equal += 1

        less_index = 0
        equal_index = num_less
        greater_index = num_less + num_equal

        res = [0] * len(nums)

        for num in nums:
            if num < pivot:
                res[less_index] = num
                less_index += 1
            elif num == pivot:
                res[equal_index] = num
                equal_index += 1
            else:
                res[greater_index] = num
                greater_index += 1

        return res
