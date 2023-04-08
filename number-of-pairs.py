class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [x - y for x, y in zip(nums1, nums2)]
        arr, res = self.merge_sort(nums, 0, len(nums), diff)
        return res


    def count(self, left_half, right_half, diff):
        right = 0
        res = 0

        for num in left_half:
            while right < len(right_half) and right_half[right] < num-diff:
                right += 1

            res += len(right_half) - right

        return res

    def merge(self, left_half, right_half):
        left = right = 0
        res = []

        while left < len(left_half) and right < len(right_half):
            if left_half[left] <= right_half[right]:
                res.append(left_half[left])
                left += 1
            else:
                res.append(right_half[right])
                right += 1

        res += left_half[left:]
        res += right_half[right:]

        return res

    def merge_sort(self, nums, left, right, diff):
        if right - left <= 1:
            return nums[left:right], 0

        mid = (left + right) // 2

        left, l_count = self.merge_sort(nums, left, mid, diff)
        right, r_count = self.merge_sort(nums, mid, right, diff)

        curr_count = self.count(left, right, diff)
        res = self.merge(left, right)

        return res, curr_count + l_count + r_count
                


    
