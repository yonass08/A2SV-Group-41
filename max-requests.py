class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        for i in range(len(requests)+1):
            for comb in combinations(requests, i):
                if self.check_combination(comb, n):
                    res = max(res, len(comb))

        return res

    def check_combination(self, comb, n):
        arr = [0] * n

        for start, end in comb:
            arr[start] -= 1
            arr[end] += 1

        return sum([abs(x) for x in arr]) == 0
