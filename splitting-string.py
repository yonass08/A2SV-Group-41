class Solution:
    def splitString(self, s: str) -> bool:
        res = []
        for i in range(1, len(s)):
            val = int(s[:i])
            res.append(val)
            if self.backtrack(s, i, res):
                return True
            res.pop()

        return False
        

    def backtrack(self, s, idx, res):
        if idx == len(s):
            return True
        for i in range(idx + 1, len(s)+1):
            val = int(s[idx: i])

            if res == [] or res[-1] - 1 == val:
                res.append(val)
                if self.backtrack(s, i, res):
                    return True
                res.pop()

        return False
