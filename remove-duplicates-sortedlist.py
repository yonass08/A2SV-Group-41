class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 0
        seeker = 1

        while seeker < len(nums):
            if nums[holder] == nums[seeker]:
                seeker += 1
            else:
                holder += 1
                nums[holder] = nums[seeker]
                seeker += 1

        return holder + 1

