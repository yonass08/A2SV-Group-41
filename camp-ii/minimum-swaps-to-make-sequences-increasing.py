class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap = [float('inf')] * n
        no_swap = [float('inf')] * n
        
        swap[-1] = 1
        no_swap[-1] = 0
        
        for i in range(n-2, -1, -1):
            if nums1[i] < nums1[i+1] and nums2[i] < nums2[i+1]:
                swap[i] = 1 + swap[i+1]
                no_swap[i] = no_swap[i+1]
                
            if nums1[i] < nums2[i+1] and nums2[i] < nums1[i+1]:
                swap[i] = min(swap[i], 1 + no_swap[i+1])
                no_swap[i] = min(no_swap[i], swap[i+1])
                
        return min(swap[0], no_swap[0])
            
            