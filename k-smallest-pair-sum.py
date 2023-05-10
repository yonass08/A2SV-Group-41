class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        first = (nums1[0] + nums2[0], 0, 0)
        heap = [first]
        seen = set(heap)

        while heap and len(res) < k:
            val, i, j = heapq.heappop(heap)
            res.append((nums1[i], nums2[j]))

            if i+1 < len(nums1):
                next1 = (nums1[i+1] + nums2[j], i+1, j)
                if next1 not in seen:
                    heapq.heappush(heap, next1)
                    seen.add(next1)
            
            if j+1 < len(nums2):
                next2 = (nums1[i] + nums2[j+1], i, j+1)
                if next2 not in seen:
                    heapq.heappush(heap, next2)
                    seen.add(next2)

        return res
