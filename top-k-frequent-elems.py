class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = list(count.keys())
        idx = self.findKth(arr, count, 0, len(arr)-1, k)
        return arr[idx:]
        
    def partition(self, nums, count, start, end):
        pivot = nums[end]
        holder = start

        for seeker in range(start, end):
            if count[nums[seeker]] < count[pivot]:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1

        nums[end], nums[holder] = nums[holder], nums[end]
        return holder

    def findKth(self, nums, count, start, end, k):
        pivot_idx = self.partition(nums, count, start, end)

        if end - pivot_idx + 1 == k:
            return pivot_idx
        elif end - pivot_idx + 1 < k:
            return self.findKth(nums, count, start, pivot_idx-1, k - end + pivot_idx - 1)
        else:
            return self.findKth(nums, count, pivot_idx+1, end, k)
