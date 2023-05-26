
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dirns = [1, 0, -1, 0, 1]
        srow, scol = 0, 0
        isInbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for row in range(len(grid)):
            if 1 in grid[row]:
                srow, scol = row, grid[row].index(1)

        grid[srow][scol] = 2
        queue1 = deque([(srow, scol)])
        queue2 = deque()

        while queue1:
            row, col = queue1.popleft()

            for i in range(4):
                nrow, ncol = row + dirns[i], col + dirns[i+1]
                if not isInbound(nrow, ncol):
                    continue
                if grid[nrow][ncol] == 0:
                    grid[nrow][ncol] = 2
                    queue2.append((nrow, ncol))
                elif grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    queue1.append((nrow, ncol))

        res = 1

        while queue2:
            for _ in range(len(queue2)):
                row, col = queue2.popleft()

                for i in range(4):
                    nrow, ncol = row + dirns[i], col + dirns[i+1]
                    if not isInbound(nrow, ncol):
                        continue
                    if grid[nrow][ncol] == 0:
                        grid[nrow][ncol] = 2
                        queue2.append((nrow, ncol))
                    elif grid[nrow][ncol] == 1:
                        return res

            res += 1

        return -1
                    

