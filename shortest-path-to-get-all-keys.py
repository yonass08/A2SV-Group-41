class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirns = [1, 0, -1, 0, 1]
        isInbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        key = lambda ch: 1 << ord(ch) - ord('a') 
        lock = lambda ch: 1 << ord(ch) - ord('A') 

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "@":
                    srow, scol = row, col
                elif grid[row][col].islower():
                    count += 1

        all_keys = 2 ** count - 1

        queue = deque([(srow, scol, 0)])
        seen = set(queue)

        res = 0

        while queue:
            for _ in range(len(queue)):
                row, col, keys = queue.popleft()
                if keys == all_keys:
                    return res

                for i in range(4):
                    nrow, ncol = row + dirns[i], col + dirns[i+1]

                    if not isInbound(nrow, ncol) or grid[nrow][ncol] == '#'\
                     or (nrow, ncol, keys) in seen:
                        continue
                    
                    if grid[nrow][ncol].islower():
                        cKey = keys | key(grid[nrow][ncol])
                        queue.append((nrow, ncol, cKey))
                        seen.add((nrow, ncol, cKey))
                    elif grid[nrow][ncol].isupper():
                        if keys & lock(grid[nrow][ncol]):
                            queue.append((nrow, ncol, keys))
                            seen.add((nrow, ncol, keys))
                    else:
                        queue.append((nrow, ncol, keys))
                        seen.add((nrow, ncol, keys))
            res += 1
        
        return -1

