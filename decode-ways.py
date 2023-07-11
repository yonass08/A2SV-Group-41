class Solution:
    def numDecodings(self, s: str) -> int:
        res = [1] * (len(s)+1)

        if s[-1] == '0':
            res[-2] = 0

        for i in range(len(res)-3, -1, -1):
            res[i] = res[i+1]

            if int(s[i: i+2]) <= 26:
                res[i] += res[i+2]

            if s[i] == '0':
                res[i] = 0

        return res[0]
