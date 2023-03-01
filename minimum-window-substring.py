class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [0, len(s)+1]
        t_counter = Counter(t)
        to_find = len(t_counter)

        left = 0
        for right in range(len(s)):
            if s[right] in t_counter:
                t_counter[s[right]] -= 1
                if t_counter[s[right]] == 0:
                    to_find -= 1

            while to_find == 0:
                if right - left < res[1] - res[0]:
                    res = [left, right]

                if s[left] in t_counter:
                    t_counter[s[left]] += 1
                    if t_counter[s[left]] == 1:
                        to_find += 1
                left += 1

        if res == [0, len(s) + 1]:
            return ''

        return s[res[0]:res[1]+1]
