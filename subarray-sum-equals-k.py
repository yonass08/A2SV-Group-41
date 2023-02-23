class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0 
        currentSum = 0
        prefixes = defaultdict(int)
        prefixes[0] = 1
        
        for i in nums:
            currentSum += i
            diff = currentSum - k
            answer += prefixes[diff]
            prefixes[currentSum] += 1
            
        return answer
