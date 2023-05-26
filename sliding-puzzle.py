class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(board[0] + board[1])

        queue = deque([start])
        seen = set(queue)
        res = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == (1, 2, 3, 4, 5, 0):
                    return res

                for nex in self.nextMoves(curr):
                    if nex not in seen:
                        queue.append(nex)
                        seen.add(nex)
            res += 1

        return -1
        
    def nextMoves(self, curr):
        res = []
        dirns = [1, 0, -1, 0, 1]

        idx = curr.index(0)
        row, col = idx // 3, idx % 3

        for i in range(4):
            nrow, ncol = row+dirns[i], col+dirns[i+1]
            if not (0 <= nrow < 2 and 0 <= ncol < 3):
                continue

            switch = nrow * 3 + ncol
            nex = list(curr)
            nex[idx], nex[switch] = nex[switch], nex[idx]
            res.append(tuple(nex))

        return res
