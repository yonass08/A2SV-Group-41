class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_sort = [(interval[0], idx) for idx, interval in enumerate(intervals)]
        start_sort.sort()

        res = []

        for start, end in intervals:
            low = 0
            high = n-1 

            while low <= high:
                mid = low + (high - low) // 2

                if start_sort[mid][0] >= end:
                    high = mid - 1
                else:
                    low = mid + 1

            res.append(start_sort[low][1] if low < n else -1)

        return res 
