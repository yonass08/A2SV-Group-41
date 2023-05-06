class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg = [-x for x in stones]
        heapq.heapify(neg)

        while len(neg) > 1:
            y = heapq.heappop(neg)
            x = heapq.heappop(neg)

            if y - x < 0:
                heapq.heappush(neg, y-x)

        if neg:
            return -neg[0]
        
        return 0