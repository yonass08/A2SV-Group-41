class Solution:
    def __init__(self):
        self.parent ={chr(ch): chr(ch) for ch in range(ord('a'), ord('z')+1)}
        self.size = defaultdict(lambda: 1)


    def equationsPossible(self, equations: List[str]) -> bool:
        notEqual = []

        for equation in equations:
            if equation[1] == '!':
                notEqual.append((equation[0], equation[3]))
            else:
                self.union(equation[0], equation[3])

        for a, b in notEqual:
            if self.find(a) == self.find(b):
                return False

        return True
        


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