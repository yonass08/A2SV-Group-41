class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        res = []
        dirn = 1

        row, col = 0, 0

        while row + col < m + n - 1:
            res.append(mat[row][col])

            col += dirn
            row -= dirn

            # going off in the right direction
            if col == n:
                col -= 1
                row += 2
                dirn = -1

            # going off in the top direction
            elif row < 0:
                row += 1
                dirn = -1

            # going off in the bottom direction
            elif row == m:
                row -= 1
                col += 2
                dirn = 1

            # going off in the left direction
            elif col < 0:
                col += 1
                dirn = 1

        return res

