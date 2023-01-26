class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def area(i, j):
            return (j - i) * min(height[i], height[j])
        
        max_area = 0
        low, hi = 0, len(height) - 1
        
        while low < hi:
            max_area = max(max_area, area(low, hi))
            if height[low] < height[hi]:
                low += 1
            else:
                hi -= 1
        
    
        return max_area
