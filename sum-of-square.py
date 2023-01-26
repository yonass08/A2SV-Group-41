class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num = 2
        while c >= num * num:
            count = 0
            while c % num == 0:
                count += 1
                c //= num

            if count % 2 == 1 and num % 4 == 3:
                return False

            num += 1

        if c > 1 and c%4 == 3:
            return False

        return True 
