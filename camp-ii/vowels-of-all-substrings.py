class Solution:
    def countVowels(self, word: str) -> int:
        vowels = "aeiou"
        res = 0
        prev = 0
        
        for i, ch in enumerate(word):
            curr = prev
            if ch in vowels:
                curr += i+1
            res += curr
            prev = curr
                     
        return res
                
        