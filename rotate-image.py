class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for row in range(n//2 + n%2):
            for col in range(n//2):
                temp = matrix[row][col]
                matrix[row][col] = matrix[-col-1][row]
                matrix[-col-1][row] = matrix[-row-1][-col-1]
                matrix[-row-1][-col-1] = matrix[col][-row-1]
                matrix[col][-row-1] = temp
