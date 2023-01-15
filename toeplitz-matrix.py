class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows-1):
            for col in range(cols-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False

        return True

