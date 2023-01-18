class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        start_row = 0
        start_col = 0

        end_row = len(matrix)-1
        end_col = len(matrix[0])-1

        total_size = len(matrix) * len(matrix[0])

        while len(res) < total_size:
            for col in range(start_col, end_col+1):
                res.append(matrix[start_row][col])
            start_row += 1

            for row in range(start_row, end_row+1):
                res.append(matrix[row][end_col])
            end_col -= 1

            if len(res) == total_size:
                break

            for col in range(end_col, start_col-1, -1):
                res.append(matrix[end_row][col])
            end_row -= 1

            for row in range(end_row, start_row-1, -1):
                res.append(matrix[row][start_col])
            start_col += 1

        return res

             
