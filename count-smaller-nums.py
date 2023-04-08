class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for _, idx, count in self.mergeSort(nums, 0, len(nums)):
            res[idx] = count
        return res

    def updateCount(self, left, right):
        rightPointer = 0

        for triple in left:
            while rightPointer < len(right) and right[rightPointer] < triple:
                rightPointer += 1

            triple[2] += rightPointer

        return 

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
        if end - start == 1:
            return [[nums[start], start, 0]]

        mid = (start + end) // 2

        left = self.mergeSort(nums, start, mid)
        right = self.mergeSort(nums, mid, end)

        self.updateCount(left, right)
        return self.merge(left, right)




