class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = (len(b) + len(a) - 1) // len(a)
        
        def contains(s, x):
            LPS = [0] * len(s)
        
            for j in range(1, len(x)):
                pos = LPS[j-1]

                while pos > 0 and x[pos] != x[j]:
                    pos = LPS[pos-1]

                if x[j] == x[pos]:
                    LPS[j] = pos + 1

            j = 0
            
            for i in range(len(s)):
                if j == len(x):
                    return True
                    
                while j > 0 and s[i] != x[j]:
                    j = LPS[j-1]
                    
                if s[i] == x[j]:
                    j += 1
                
            return j == len(x)
                    
        base = a * times   

        if contains(base, b):
            return times
        if contains(base + a, b):
            return times + 1
        return -1