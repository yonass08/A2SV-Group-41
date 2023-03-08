class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_f = sorted([word.count(min(word)) for word in words])

        res = []
        for query in queries:
            query_f = query.count(min(query))

            low = 0
            high = len(words_f) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if words_f[mid] <= query_f:
                    low = mid + 1
                else:
                    high = mid - 1

            res.append(len(words_f) - low)

        return res
 
