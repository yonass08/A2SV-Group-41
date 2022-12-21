class Solution:
    def similarPairs(self, words: List[str]) -> int:
        base = ord('a')
        for i in range(len(words)):
            item = 0
            for x in words[i]:
                item |= 1 << (ord(x) - base)
            words[i] = item
        counter = Counter(words)

        res = 0
        print(counter)
        for word in counter:
            res += counter[word] * (counter[word] - 1) // 2

        return res
