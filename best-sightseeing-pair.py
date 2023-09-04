class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = [0] * len(values)
        maximum = [0] * len(values)

        res[-2] = values[-1] + values[-2] - 1
        maximum[-2] = max(values[-2] - 1, values[-1] - 2)

        for i in range(len(values)-3, -1, -1):
            res[i] = max(res[i+1], values[i] + maximum[i+1])
            maximum[i] = max(values[i], maximum[i+1]) - 1

        return res[0]
        