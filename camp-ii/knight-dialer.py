class Solution:
    def knightDialer(self, n: int) -> int:
        possible = {
                        0: [4, 6],
                        1: [6, 8],
                        2: [7, 9],
                        3: [4, 8],
                        4: [0, 3, 9],
                        5: [],
                        6: [0, 1, 7],
                        7: [2, 6],
                        8: [1, 3],
                        9: [2, 4]
                    }
        @cache
        def dp(num, n):
            if n == 0:
                return 1
            
            res = 0
            for pos in possible[num]:
                res = (res + dp(pos, n-1)) % (10 ** 9 + 7)
                
            return res
        
        res = 0
        for num in range(10):
            res = (res + dp(num, n-1)) % (10 ** 9 + 7)
            
        return res
        