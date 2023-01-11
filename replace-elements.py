class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        # Create a hash table that maps every number to it's index
        index_map = {}
        for index, num in enumerate(nums):
            index_map[num] = index

        # Perform each replacement operation
        for replaced, replacer in operations:
            nums[index_map[replaced]] = replacer
            index_map[replacer] = index_map[replaced]
            del index_map[replaced]

        return nums
