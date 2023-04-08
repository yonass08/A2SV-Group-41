class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = 0
        def orArray(arr):
            res = 0
            for num in arr:
                res  |= num
            return res

        total = orArray(nums)
        for i in range(1, len(nums)+1):
            for comb in combinations(nums, i):
                if orArray(comb) == total:
                    res += 1

        return res

