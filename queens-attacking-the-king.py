class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [([False] * 8) for _ in range(8)]
        for queen in queens:
            board[queen[0]][queen[1]] = True

        directions = [-1, 0, 1]

        res = []

        for x_dirn in directions:
            for y_dirn in directions:
                if x_dirn == 0 and y_dirn == 0:
                    continue

                row = king[0] + y_dirn
                col = king[1] + x_dirn

                while 0 <= col < 8 and 0 <= row < 8:
                    if board[row][col]:
                        res.append([row, col])
                        break
                    row += y_dirn
                    col += x_dirn

        return res

        
