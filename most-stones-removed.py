class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.parent = defaultdict(int)
        self.size = defaultdict(int)

        for a, b in stones:
            self.parent[a] = a
            self.parent[-b-1] = -b-1
            self.size[a] = 1
            self.size[-b-1] = 1

        for a, b in stones:
            self.union(a, -b-1)

        res = len(stones)
        for x in self.parent:
            if self.parent[x] == x:
                res -= 1

        return res


    def find(self, x):
        hold = x
        while self.parent[x] != x:
            x = self.parent[x]

        while self.parent[hold] != x:
            temp = self.parent[hold]
            self.parent[hold] = x
            hold = temp

        return x

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.size[xroot] > self.size[yroot]:
            self.parent[yroot] = xroot
            self.size[xroot] += self.size[yroot]
        else:
            self.parent[xroot] = yroot
            self.size[yroot] += self.size[xroot]