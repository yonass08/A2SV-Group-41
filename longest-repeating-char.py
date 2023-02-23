class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        slow = 0
        largest = 0
        
        def index(ch):
            return ord(ch) - ord('A')
        
        for fast in range(len(s)):
            chars[index(s[fast])] += 1
            largest = max(largest, chars[index(s[fast])])
            
            if largest + k <= fast - slow:
                chars[index(s[slow])] -= 1
                slow += 1
   
        return fast - slow + 1

#40min
