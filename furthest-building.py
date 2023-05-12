class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        idx = 0

        while idx < len(heights)-1:
            if heights[idx+1] > heights[idx]:
                heappush(heap, heights[idx+1] - heights[idx])
                if len(heap) > ladders:
                    least = heappop(heap)
                    if bricks < least:
                        break
                    bricks -= least
            idx += 1

        return idx