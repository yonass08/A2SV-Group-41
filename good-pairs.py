class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        count = 0

        for num in counter:
            count += counter[num] * (counter[num]-1) // 2
                    
        return count
