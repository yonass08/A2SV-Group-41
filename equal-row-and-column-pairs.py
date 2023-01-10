class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0

        rowCounter = Counter(tuple(row) for row in grid)

        gridTranspose = zip(*grid)

        for col in gridTranspose:
            res += rowCounter[col]

        return res
