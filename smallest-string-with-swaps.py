class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = [i for i in range(len(s))]
        self.size = [1] * len(s)

        for a, b in pairs:
            self.union(a, b)


        letters = defaultdict(list)
        indices = defaultdict(list)

        for i in range(len(s)):
            root = self.find(i)
            letters[root].append(s[i])
            indices[root].append(i)

        res = [''] * len(s)

        for root in indices:
            letters[root].sort()
            indices[root].sort()

            for i in range(len(indices[root])):
                res[indices[root][i]] = letters[root][i]

        return "".join(res)


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