class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirns = [1, 0, -1, 0, 1]
        queue = deque()

        res = [[-1] * len(mat[0]) for _ in range(len(mat))]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    res[row][col] = -2

        isInbound = lambda row, col: 0 <= row < len(mat) and 0 <= col < len(mat[0])
        dist = 0

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                res[row][col] = dist

                for i in range(4):
                    nrow = row + dirns[i]
                    ncol = col + dirns[i+1]

                    if not isInbound(nrow, ncol) or res[nrow][ncol] != -1:
                        continue

                    queue.append((nrow, ncol))
                    res[nrow][ncol] = -2
            dist += 1

        return res




        