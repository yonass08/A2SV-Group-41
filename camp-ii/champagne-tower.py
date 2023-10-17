class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        rows = 100
        glasses = [[0] * (i + 1) for i in range(rows)]

        glasses[0][0] = poured


        for i in range(rows - 1):
            for j in range(i + 1):
                overflow = max(0, glasses[i][j] - 1)
                glasses[i][j] -= overflow

                glasses[i + 1][j] += overflow / 2
                glasses[i + 1][j + 1] += overflow / 2

        target_glass = glasses[query_row][query_glass]

        return target_glass
        