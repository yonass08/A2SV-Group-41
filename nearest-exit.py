class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def isAllowed(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == '.'

        def isExit(row, col):
            if [row, col] == entrance:
                return False

            if row == 0 or row == len(maze)-1:
                return True

            if col == 0 or col == len(maze[0])-1:
                return True

            return False

        dirns = [1, 0, -1, 0, 1]

        queue = deque([entrance])
        maze[entrance[0]][entrance[1]] = 'v'

        res = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if isExit(row, col):
                    return res

                for i in range(4):
                    nrow, ncol = row + dirns[i], col + dirns[i+1]

                    if isAllowed(nrow, ncol):
                        queue.append([nrow, ncol])
                        maze[nrow][ncol] = 'v'

            res += 1

        return -1