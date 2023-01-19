class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        idx = 0

        while idx < len(arr)-1 and arr[idx+1] > arr[idx]:
            idx += 1

        if idx == 0 or idx == len(arr)-1:
            return False

        for i in range(idx, len(arr) - 1):
            if arr[i] <= arr[i+1]:
                return False

        return True
