
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 0
        res = 0

        if len(arr) == 1:
            return 1

        while right < len(arr):
            while right < len(arr)-1 and\
             (arr[right-1]>arr[right]<arr[right+1] or arr[right-1]<arr[right]>arr[right+1]):
                right += 1
            while left < right and arr[left] == arr[left+1]:
                left += 1
            res = max(res, right - left + 1)
            
            left = right
            right += 1

        return res

