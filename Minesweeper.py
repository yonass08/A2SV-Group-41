class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirns = [1, -1, -1, 1, 1, 0, -1, 0, 1]
        isInbound = lambda row, col: 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            
            count = 0
            for i in range(8):
                r_next, c_next = row + dirns[i], col + dirns[i+1]
                if isInbound(r_next, c_next):
                    count += board[r_next][c_next] == 'M'

            if count > 0:
                board[row][col] = str(count)
                return

            board[row][col] = 'B'
            for i in range(8):
                r_next, c_next = row + dirns[i], col + dirns[i+1]
                if isInbound(r_next, c_next) and board[r_next][c_next] == 'E':
                    dfs(r_next, c_next)

        dfs(*click)
        return board