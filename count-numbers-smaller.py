class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0] * 102
        result = []
        for num in nums:
            counter[num+1] += 1

        for num in range(1, 101):
            counter[num] += counter[num-1]

        for num in nums:
            result.append(counter[num])
        return result
