class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = lambda ch: ord(ch) - ord('a') + 1
        
        curr = val(s[n-k]) % modulo
        p = 1
        for i in range(n-k+1, n):
            p = (p * power) % modulo
            curr = (curr + p * val(s[i])) % modulo
        
        if curr == hashValue:
            res = n-k
        
        for i in range(n-k-1, -1, -1):
            curr = ((curr - (p * val(s[i+k]))) * power + val(s[i])) % modulo
            if curr == hashValue:
                res = i
                
        return s[res: res+k]
            
        
        