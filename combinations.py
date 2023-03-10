class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb, combs = [], []

        def backtrack(i, curComb, combs, n, k):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return

            for j in range(i, n + 1):
                curComb.append(j)
                backtrack(j + 1, curComb, combs, n, k)
                curComb.pop()

        backtrack(1, curComb, combs, n, k)
        return combs
