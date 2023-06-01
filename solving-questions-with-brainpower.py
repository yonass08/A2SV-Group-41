class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        bestRight = [0] * len(questions)
        best = 0

        for i in range(len(questions)-1, -1, -1):
            bestRight[i] = questions[i][0]
            if i + questions[i][1] + 1 < len(bestRight):
                bestRight[i] += bestRight[i + questions[i][1] + 1]

            best = bestRight[i] = max(best, bestRight[i])

        return best