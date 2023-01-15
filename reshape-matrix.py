class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        res = [[0] * c for _ in range(r)]
        mat_row = 0
        mat_col = 0

        for res_row in range(r):
            for res_col in range(c):
                res[res_row][res_col] = mat[mat_row][mat_col]
                if mat_col == n-1:
                    mat_row += 1
                    mat_col = 0
                else:
                    mat_col += 1

        return res
