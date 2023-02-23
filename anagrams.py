class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        to_find = len(counter)
        res = []

        for idx in range(len(s)):
            counter[s[idx]] -= 1
            if counter[s[idx]] == 0:
                to_find -= 1

            if to_find == 0:
                res.append(idx-len(p)+1)

            if idx >= len(p)-1:
                counter[s[idx-len(p)+1]] += 1
                if counter[s[idx-len(p)+1]] == 1:
                    to_find += 1

        return res
        
