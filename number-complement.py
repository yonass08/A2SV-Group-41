class Solution:
    def findComplement(self, num: int) -> int:
        curr = 1
        prev = num

        while curr <= num:
            prev = prev ^ curr
            curr <<= 1

        return prev
