class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = [(-counter[word], word) for word in counter]
        heapify(heap)

        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])


        return res
        
