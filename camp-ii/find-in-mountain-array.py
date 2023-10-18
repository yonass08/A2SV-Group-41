# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        low = 1
        high = length - 2
        
        while low <= high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid - 1
                
        peak = low


        low = 0
        high = peak
        while low <= high:
            mid = (low + high) // 2
            
            if mountain_arr.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1    
 

        if mountain_arr.get(low) == target:
            return low
        
        low = peak + 1
        high = length - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if mountain_arr.get(mid) > target:
                low = mid + 1
            else:
                high = mid - 1

        if low < length and mountain_arr.get(low) == target:
            return low
        
        return -1