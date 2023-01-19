class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num_set = set(nums)
        for num in nums:
            num_set.add(int(str(num)[::-1]))

        return len(num_set)
