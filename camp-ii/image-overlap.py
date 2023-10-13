class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        
        isInbound = lambda row, col: 0 <= row < n and 0 <= col < n

        def countOverlap(sr, sc):
            overlaps = 0
            
            for row in range(n):
                for col in range(n):
                    if isInbound(row-sr, col-sc) and A[row-sr][col-sc] == B[row][col] == 1:
                        overlaps += 1
                        
            return overlaps
        
        res = 0
        
        for sr in range(-n+1, n):
            for sc in range(-n+1, n):
                res = max(res, countOverlap(sr, sc))
                
        return res
                    