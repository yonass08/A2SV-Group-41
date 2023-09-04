class Solution:
    def __init__(self):
        self.memo = {}
        self.dirns = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1

        if (k, row, column) in self.memo:
            return self.memo[(k, row, column)]

        isInbound = lambda r, c: 0 <= r < n and 0 <= c < n
        res = 0

        for r, c in self.dirns:
            nrow = row + r
            ncol = column + c

            if isInbound(nrow, ncol):
                res += self.knightProbability(n, k-1, nrow, ncol)

        self.memo[(k, row, column)] = res / 8
        return res / 8



        