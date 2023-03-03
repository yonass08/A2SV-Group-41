class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.recursive_reverse(s, 0, len(s)-1)
        
        
    def recursive_reverse(self, s, start, end):
        if start >= end:
            return
        self.recursive_reverse(s, start+1, end-1)
        s[start], s[end] = s[end], s[start]
