class Solution:
    def strStr(self, haystack: str, needle: str) -> int:    
        prime = 10**9 + 7
        base = 27
        window = 0
        poll = pow(base, len(needle)-1, prime)

        comp = 0

        for ch in needle:
            comp = (comp * base + ord(ch) - ord('a') + 1) % prime

        for i in range(len(haystack)):
            ch = haystack[i]
            if i < len(needle) - 1 :
                window = (window * base + ord(ch) - ord('a') + 1) % prime
            else:
                window = (window * base + ord(ch) - ord('a') + 1) % prime
                # print(comp, window)
                if window == comp and haystack[i-len(needle)+1:i+1] == needle:
                    return i - len(needle) + 1
                num = ord(haystack[i - len(needle) + 1]) - ord('a') + 1
                window = (window - (num * poll)) % prime


        return -1



        return -1

            
        
        