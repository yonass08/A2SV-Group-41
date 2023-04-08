class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKth(nums, 0, len(nums)-1, k)
        
    def partition(self, nums, start, end):
        pivot = nums[end]
        holder = start

        for seeker in range(start, end):
            if nums[seeker] < pivot:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1

        nums[end], nums[holder] = nums[holder], nums[end]
        return holder

    def findKth(self, nums, start, end, k):
        pivot_idx = self.partition(nums, start, end)

        if end - pivot_idx + 1 == k:
            return nums[pivot_idx]
        elif end - pivot_idx + 1 < k:
            return self.findKth(nums, start, pivot_idx-1, k - end + pivot_idx - 1)
        else:
            return self.findKth(nums, pivot_idx+1, end, k)
            
