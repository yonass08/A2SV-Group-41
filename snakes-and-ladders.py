class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get(num):
            row = (num + n - 1) // n
            if row % 2 == 1:
                col = (num-1) % n
            else:
                col = n - ((num-1) % n) - 1

            return board[n-row][col]

        seen = [False] * (n**2 + 1)
        queue = deque([1])
        seen[1] = True

        count = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == n**2:
                    return count

                for i in range(curr+1, min(curr+6, n**2)+1):
                    val = get(i)
                    nex = val if val != -1 else i

                    if not seen[nex]:
                        queue.append(nex)
                        seen[nex] = True
            
            count += 1

        return -1
