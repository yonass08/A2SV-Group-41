class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapify(heap)

        for _ in range(k):
            curr = heappop(heap)
            heappush(heap, curr // 2)

        return -sum(heap)