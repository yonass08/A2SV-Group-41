class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        while low <= high:
            mid = low + (high - low) // 2
            res = sum([(num + mid - 1) // mid for num in nums])

            if res <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low
