class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex+1)

        for idx in range(1, len(res)):
            res[idx] = ((rowIndex - idx + 1) * (res[idx-1])) // (idx)

        return res
