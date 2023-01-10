class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        num_X = board[0].count('X') + board[1].count('X') + board[2].count('X')
        num_O = board[0].count('O') + board[1].count('O') + board[2].count('O')

        if num_X - num_O > 1 or num_X - num_O < 0:
            return False

        X_winner = False
        O_winner = False

        # check if there is a horizontal winner
        if board[0][0] == board[0][1] == board[0][2]:
            if board[0][0] == 'X': X_winner = True
            if board[0][0] == 'O': O_winner = True

        if board[1][0] == board[1][1] == board[1][2]:
            if board[1][0] == 'X': X_winner = True
            if board[1][0] == 'O': O_winner = True

        if board[2][0] == board[2][1] == board[2][2]:
            if board[2][0] == 'X': X_winner = True
            if board[2][0] == 'O': O_winner = True



        # check if there is a vertical winner
        if board[0][0] == board[1][0] == board[2][0]:
            if board[0][0] == 'X': X_winner = True
            if board[0][0] == 'O': O_winner = True

        if board[0][1] == board[1][1] == board[2][1]:
            if board[0][1] == 'X': X_winner = True
            if board[0][1] == 'O': O_winner = True

        if board[0][2] == board[1][2] == board[2][2]:
            if board[0][2] == 'X': X_winner = True
            if board[0][2] == 'O': O_winner = True



        #check if there is a diagonal winner
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X': X_winner = True
            if board[0][0] == 'O': O_winner = True

        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'X': X_winner = True
            if board[0][2] == 'O': O_winner = True

        if X_winner and O_winner:
            return False
        elif X_winner:
            return num_X - num_O == 1
        elif O_winner:
            return num_X - num_O == 0

        return True
