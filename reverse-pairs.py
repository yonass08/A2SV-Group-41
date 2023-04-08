class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        _, res = self.mergeSort(nums, 0, len(nums))
        return res

    def countPairs(self, left, right):
        rightPointer = 0
        count = 0

        for num in left:
            while rightPointer < len(right) and num > 2 * right[rightPointer]:
                rightPointer += 1
            count += rightPointer

        return count

    def merge(self, left, right):
        leftPointer, rightPointer = 0, 0
        res = []

        while leftPointer < len(left) and rightPointer < len(right):
            if left[leftPointer] < right[rightPointer]:
                res.append(left[leftPointer])
                leftPointer += 1
            else:
                res.append(right[rightPointer])
                rightPointer += 1

        res += left[leftPointer:]
        res += right[rightPointer:]

        return res

    def mergeSort(self, nums, start, end):
        if end - start <= 1:
            return nums[start: end], 0

        mid = (start + end) // 2
        left, leftCount = self.mergeSort(nums, start, mid)
        right, rightCount = self.mergeSort(nums, mid, end)

        currCount = leftCount + self.countPairs(left, right) + rightCount
        return self.merge(left, right), currCount

