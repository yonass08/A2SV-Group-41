class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(idx1, idx2):
            if idx1 >= len(word1):
                return len(word2) - idx2
            
            if idx2 >= len(word2):
                return len(word1) - idx1
            
            res = int(word1[idx1] != word2[idx2]) + dp(idx1+1, idx2+1)
            res = min(res, 1 + dp(idx1+1, idx2), 1 + dp(idx1, idx2 + 1))
            
            return res
        
        return dp(0, 0)