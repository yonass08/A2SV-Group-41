class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixes = defaultdict(int)
        prefixes[0] = 1

        res = 0
        prefix = 0
        
        for num in nums:
            prefix += num
            diff = prefix - goal

            res += prefixes[diff]
            prefixes[prefix] += 1

        return res
        
