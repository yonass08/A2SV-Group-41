class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_border = 0
        top_border = 0
        right_border = len(matrix[0]) - 1
        bottom_border = len(matrix) - 1

        row, col = 0, 0
        res = []
        x_dirn = 1
        y_dirn = 0

        for _ in range(len(matrix) * len(matrix[0])):
            res.append(matrix[row][col])

            col += x_dirn
            row += y_dirn

            # going of the right border
            if col > right_border:
                y_dirn = 1
                x_dirn = 0
                col -= 1
                row += 1
                top_border += 1
            
            # going of the bottom border
            elif row > bottom_border:
                y_dirn = 0
                x_dirn = -1
                row -= 1
                col -= 1
                right_border -= 1

            # going of the left border
            elif col < left_border:
                y_dirn = -1
                x_dirn = 0
                row -= 1
                col += 1
                bottom_border -= 1

            # going of the top border
            elif row < top_border:
                y_dirn = 0
                x_dirn = 1
                row += 1
                col += 1
                left_border += 1

        return res







