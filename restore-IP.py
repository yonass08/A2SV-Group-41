class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtrack(res, [], s, 0)
        return res 

    def backtrack(self, res, curr, s, idx):
        if len(curr) == 3:
            cand = s[idx:]
            val = int(cand)

            if val < 256 and len(str(val)) == len(cand):
                ip = f'{s[:curr[0]]}.{s[curr[0]:curr[1]]}.{s[curr[1]:curr[2]]}.{s[curr[2]:]}'
                res.append(ip)
            return

        for i in range(idx+1, len(s)):
            cand = s[idx: i]
            val = int(cand)

            if val < 256 and len(str(val)) == len(cand):
                curr.append(i)
                self.backtrack(res, curr, s, i)
                curr.pop()
