class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binary_search(nums, target )
        second = self.binary_search(nums, target+1 ) - 1

        if second < first:
            return [-1, -1 ]
    
        return [first, second]

    
    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        return low
