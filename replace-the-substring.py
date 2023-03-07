class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        expected = len(s) // 4

        if all(counter[ch] == expected for ch in counter):
            return 0

        left = 0
        res = len(s) + 1

        for right in range(len(s)):
            counter[s[right]] -= 1

            while all(counter[ch] <= expected for ch in counter):
                res = min(res, right - left + 1)
                counter[s[left]] += 1
                left += 1

        return res
