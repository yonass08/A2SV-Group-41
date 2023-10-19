class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = sum(nums)
        for i in range(len(nums)-1, 0, -1):
            count = i+1
            
            cap = (tot + count - 1) // count
            if nums[i] > cap:
                diff = nums[i] - cap
                nums[i-1] += diff
                nums[i] -= diff
                
            tot -= nums[i]
            
        return max(nums)