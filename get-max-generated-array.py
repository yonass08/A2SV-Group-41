class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        res = [0, 1]

        for i in range(2, n+1):
            res.append(res[i // 2])
            if i % 2 == 1:
                res[-1] += res[i//2 + 1]

        return max(res)

         
        

    