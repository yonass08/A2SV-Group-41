class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(idx1, idx2):
            if idx1 >= len(nums1) or idx2 >= len(nums2):
                return 0
            
            
            res = 0
            for i in range(idx2, len(nums2)):
                if nums1[idx1] == nums2[i]:
                    res = 1 + dp(idx1+1, i+1)
                    break
                    
                    
            res =  max(res, dp(idx1+1, idx2))
            # print(idx1, idx2, res)
            return res
        
        return dp(0, 0)
            
        