class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
       
        inverted = 0
        while x > inverted:
            inverted = inverted*10 + x%10
            x //= 10

        return x == inverted or x == inverted // 10
