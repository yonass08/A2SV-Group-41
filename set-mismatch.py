class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        curr = 0
        missing = len(nums)+1

        while curr < len(nums):
            curr_num = nums[curr]

            if curr_num == curr + 1:
                curr += 1
            elif nums[curr_num-1] == curr_num:
                duplicate = curr_num
                missing = curr+1
                curr +=1 
            else:
                if curr_num == missing:
                    missing = curr+1
                nums[curr], nums[curr_num-1] = nums[curr_num-1], nums[curr]

        return [duplicate, missing]
