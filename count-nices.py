class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        curr_count = 0
        odd_count = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
                curr_count = 0

            while odd_count == k:
                curr_count += 1
                odd_count -= nums[left] % 2
                left += 1

            res += curr_count

        return res
