class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr), 0, -1):
            index = arr.index(i)
            if index == i-1:
                continue
            if index != 0:
                result.append(index+1)
                self.pancakeFlip(arr, index+1)
            result.append(i)
            self.pancakeFlip(arr, i)
            
        return result
    
    def pancakeFlip(self, arr, k):
        for i in range(k // 2):
            arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
