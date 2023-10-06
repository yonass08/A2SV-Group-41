class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        maxAge = max(ages)
        dp = [0]*(maxAge+1)
        infos = list(zip(scores, ages))
        infos.sort()

        for score, age in infos:
            x = age & (age-1)
            while x:
                dp[age] = max(dp[x], dp[age])
                x &= x-1

            dp[age] += score

            x = age + (age&(-age))
            while x <= maxAge:
                dp[x] = max(dp[x], dp[age])
                x += x&(-x)

        return max(dp)
