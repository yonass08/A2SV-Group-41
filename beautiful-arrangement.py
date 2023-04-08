class Solution:
    def __init__(self):
        self.count = 0

    def countArrangement(self, n: int) -> int:
        visited = [False] * (n+1);
        self.backtrack(n, 1, visited);
        return self.count
        
    def backtrack(self, n, pos, visited):
        if pos > n:
            self.count += 1
        for i in range(1, n+1):
            if (not visited[i]) and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                self.backtrack(n, pos + 1, visited);
                visited[i] = False
