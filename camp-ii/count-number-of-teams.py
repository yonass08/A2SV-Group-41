class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def countInc(rating):
            before = [0] * len(rating)

            for outer in range(1, len(rating)):
                for inner in range(outer):
                    if rating[inner] < rating[outer]:
                        before[outer] += 1
                        
            res = 0
            for outer in range(1, len(rating)):
                for inner in range(outer):
                    if rating[inner] < rating[outer]:
                        res += before[inner]
                        
            return res
        
        return countInc(rating) + countInc(rating[::-1])
                        
                    
