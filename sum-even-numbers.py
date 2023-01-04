class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        currentSum = sum([val for val in nums if val % 2 == 0])
        res = []

        for value, index in queries:
            # when the number at index is even we need to remove it
            if nums[index] % 2 == 0:
                currentSum -= nums[index]
            
            nums[index] += value

            # update currentSum based on the current value of nums[index] 
            if nums[index] % 2 == 0:
                currentSum += nums[index]
        
            res.append(currentSum)

        return res

