class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        queue = deque()
        dirn = (1, 0, -1, 0, 1)

        isInbound = lambda row, col: 0 <= row < len(image) and 0 <= col < len(image[0])
        if old_color != color:
            queue.append((sr, sc))

        while queue:
            length = len(queue)
            for i in range(length):
                row, col = queue.popleft()
                if not isInbound(row, col) or  image[row][col] != old_color:
                    continue

                image[row][col] = color
                for i in range(len(dirn) - 1):
                    queue.append((row + dirn[i], col + dirn[i+1]))

        return image


        
