class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = n & 1

        while n:
            n >>= 1
            if not (n & 1) ^ curr:
                return False
            curr = (n & 1)

        return True
