class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        first = 0
        second = 0
        res = []

        while first < len(word1) and second < len(word2):
            if word1[first:] > word2[second:]:
                res.append(word1[first])
                first += 1
            else:
                res.append(word2[second])
                second += 1

        res.extend(word1[first:])
        res.extend(word2[second:])

        return ''.join(res)
            
