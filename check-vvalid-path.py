
class Solution:
    def __init__(self):
        self.parent = None
        self.size = None

    def initialize(self, m, n):
        self.parent ={(row, col): (row, col) for col in range(n) for row in range(m)}
        self.size = defaultdict(lambda: 1)


    def find(self, node):
        hold = node

        while node != self.parent[node]:
            node = self.parent[node]

        res = node

        while self.parent[hold] != res:
            temp = self.parent[hold]
            self.parent[hold] = res
            hold = temp

        return res

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.size[rootX] <= self.size[rootX]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]


    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0]
        )
        self.initialize(m, n)

        dirns = [((0, -1), (0, 1)), ((-1, 0), (1, 0)), ((0, -1), (1, 0)), \
                ((0, 1), (1, 0)), ((0, -1), (-1, 0)), ((0, 1), (-1, 0))]

        isInbound = lambda row, col: 0 <= row < m and 0 <= col < n

        for row in range(m):
            for col in range(n):
                (r1, c1), (r2, c2) = dirns[grid[row][col]-1]
                if isInbound(row+r1, col+c1) and (-r1, -c1) in dirns[grid[row+r1][col+c1]-1]:
                    self.union((row, col), (row+r1, col+c1))

                if isInbound(row+r2, col+c2) and (-r2, -c2) in dirns[grid[row+r2][col+c2]-1]:
                    self.union((row, col), (row+r2, col+c2))

                
        return self.find((0, 0)) == self.find((m-1, n-1))
        


        