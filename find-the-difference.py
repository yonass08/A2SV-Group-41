class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in range(len(s)):
            res += ord(t[i]) - ord(s[i])
        return chr(res + ord(t[-1])) 
