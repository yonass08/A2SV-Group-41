class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, 3
        dirns = [1, 0, -1, 0, 1]
        
        for _ in range(4):
            for ch in instructions:
                if ch == 'G':
                    x += dirns[d]
                    y += dirns[d+1]
                elif ch == 'L':
                    d = (d + 1) % 4
                elif ch == 'R':
                    d = (d - 1) % 4
                    
        return x == 0 and y == 0 and d == 3
        