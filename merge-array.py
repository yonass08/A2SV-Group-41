class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m-1
        second = n-1

        for idx in range(n+m-1, -1, -1):
            if second < 0:
                break

            if first >= 0 and nums1[first] > nums2[second]:
                nums1[idx] = nums1[first]
                first -= 1
            else:
                nums1[idx] = nums2[second]
                second -= 1

        

