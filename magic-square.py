class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        count = 0

        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                if self.is_magic(grid, row, col):
                    count += 1

        return count

    def is_magic(self, grid, row, col):
        if len(grid) < 3 or len(grid[0]) < 3:
            return False

        found = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if grid[i][j] in found or grid[i][j] > 9 or grid[i][j] == 0:
                    return False
                found.add(grid[i][j])

        # Check the rows
        magic_sum = grid[row][col] + grid[row][col+1] + grid[row][col+2]
        if grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2] != magic_sum:
            return False
        if grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2] != magic_sum:
            return False

        # Check the columns
        for i in range(3):
            if grid[row][col+i] + grid[row+1][col+i] + grid[row+2][col+i] != magic_sum:
                return False


        # Check the diagonals
        if grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2] != magic_sum:
            return False
        if grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] != magic_sum:
            return False

        return True        
