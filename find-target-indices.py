class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        numsLess = 0
        targetCount = 0
        result = []
        
        for i in nums:
            if i < target:
                numsLess += 1
            elif i == target:
                targetCount += 1
                
        for i in range(targetCount):
            result.append(i + numsLess)
            
        return result
