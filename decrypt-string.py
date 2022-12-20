class Solution:
    def freqAlphabets(self, s: str) -> str:
        base = ord('a') - 1
        i = 0
        res = []
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                res.append(chr(base + int(s[i:i+2])))
                i += 3
            else:
                res.append(chr(base + int(s[i])))
                i += 1
        return ''.join(res)
