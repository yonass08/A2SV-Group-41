from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sList = SortedList()
        res = 0
        Mod = 10**9 + 7

        for num in instructions:
            left = sList.bisect_left(num)
            right = len(sList) - sList.bisect_right(num)

            sList.add(num)
            res = (res + min(left, right)) % Mod

        return res
