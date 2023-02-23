class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = defaultdict(int)
        maxCount = 0
        start = 0
        
        for end in range(len(s)):
            ch = s[end]
            start = max(start, pos[ch])
                
            pos[ch] = end + 1
            maxCount = max(maxCount, end - start + 1)
   
        return maxCount
