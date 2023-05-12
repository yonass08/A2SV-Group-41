class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][0], 0, 0)]
        seen = set((0, 0))

        count = 0

        def push(row, col):
            if row + 1 < len(matrix) and (row+1, col) not in seen:
                heappush(heap, (matrix[row+1][col], row+1, col))
                seen.add((row+1, col))
            if col + 1 < len(matrix[0]) and (row, col+1) not in seen:
                heappush(heap, (matrix[row][col+1], row, col+1))
                seen.add((row, col+1))
            
        res = 0

        while count < k:
            res, row, col = heappop(heap)
            push(row, col)
            count += 1

        return res