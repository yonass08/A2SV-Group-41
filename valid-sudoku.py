class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue

                curr_block = (row//3) * 3 + (col//3)
                # check for repitition
                if num in rows[row]:
                    return False

                if num in cols[col]:
                    return False

                if num in blocks[curr_block]:
                    return False

                # add the current element
                rows[row].add(num)
                cols[col].add(num)                   
                blocks[curr_block].add(num)

        return True



