class Solution:
    def maxProduct(self, words: List[str]) -> int:
        intMap = []
        for word in words:
            num = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                num |= 1 << idx
            intMap.append(num)

        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if intMap[i] & intMap[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))

        return res
