class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        curr_sum = 0

        for idx in range(len(nums)):
            curr_sum += nums[idx]

            if idx >= k-1:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[idx-k+1]

        return max_sum / k
        
