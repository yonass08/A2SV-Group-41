class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        evencount = Counter(nums[::2])
        evencount['*'] = 0
        oddcount = Counter(nums[1::2])
        oddcount['*'] = 0
        
        evenfreq = evencount.most_common()
        oddfreq = oddcount.most_common()
        
        if evenfreq[0][0] != oddfreq[0][0]:
            return n - evenfreq[0][1] - oddfreq[0][1]
        
        return min(n - evenfreq[1][1] - oddfreq[0][1], n - evenfreq[0][1] - oddfreq[1][1])
        
        