class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = (x+1) // 2

        while low <= high:
            mid = (low + high) // 2

            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid

        return high
