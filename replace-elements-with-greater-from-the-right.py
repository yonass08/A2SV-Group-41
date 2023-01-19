class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for index in range(len(arr)-1, -1, -1):
            temp = arr[index]
            arr[index] = largest
            largest = max(largest, temp)

        return arr
