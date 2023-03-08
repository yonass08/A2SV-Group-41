class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)

        while low <= high:
            mid = low + (high - low) // 2

            if citations[-mid] >= mid:
                low = mid + 1
            else:
                high = mid - 1

        return high
