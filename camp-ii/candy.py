class Solution:
    def candy(self, ratings: List[int]) -> int:
        tup = [(num, idx) for idx, num in enumerate(ratings)]
        tup.sort()
        res = [1] * len(ratings)
        
        for num, idx in tup:            
            if idx - 1 >= 0 and num > ratings[idx-1]:
                res[idx] = max(res[idx], res[idx-1] + 1)
            if idx + 1 < len(ratings) and num > ratings[idx+1]:
                res[idx] = max(res[idx], res[idx+1] + 1)
                
        return sum(res)