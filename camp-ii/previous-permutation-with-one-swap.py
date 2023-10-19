class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        while i > 0 and arr[i] >= arr[i-1]:
            i -= 1
            
        if i == 0:
            return arr
        
        idx = i-1
        swap = len(arr) - 1
        
        while arr[swap] >= arr[idx]:
            swap -= 1
            
        while arr[swap] == arr[swap-1]:
            swap -= 1
            
        arr[idx], arr[swap] = arr[swap], arr[idx]
        
        return arr
        
        