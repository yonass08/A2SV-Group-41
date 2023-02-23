class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        
        matrix.append([0] * (cols))
        for row in matrix:
            row.append(0)

        for row in range(rows):
            for col in range(cols):
                matrix[row][col] += matrix[row-1][col] + matrix[row][col-1] \
                                 - matrix[row-1][col-1]

        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2][col2] - self.matrix[row1-1][col2]\
             + self.matrix[row1-1][col1-1] - self.matrix[row2][col1-1]

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
