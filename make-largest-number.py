class NumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = [str(num) for num in nums]        
        largest_num =  "".join(sorted(nums, key = NumKey))
        return '0' if largest_num[0] == "0" else largest_num
        
