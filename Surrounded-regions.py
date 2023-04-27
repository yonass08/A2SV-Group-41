class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        isInbound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        dirn = [1, 0, -1, 0, 1]

        def dfs(row, col):
            if not isInbound(row, col) or board[row][col] != 'O':
                return

            board[row][col] = 'N'
            for i in range(4):
                dfs(row + dirn[i], col + dirn[i+1])

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)

        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'N':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'

    
