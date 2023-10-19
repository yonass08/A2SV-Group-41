class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0] * len(s)
        
        for j in range(1, len(s)):
            pos = LPS[j-1]
            
            while pos > 0 and s[pos] != s[j]:
                pos = LPS[pos-1]
                
            if s[j] == s[pos]:
                LPS[j] = pos + 1
                
        return s[:LPS[-1]]
            
        