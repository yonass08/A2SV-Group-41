class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res = -1
        cycleNumber = [-1] * len(edges)
        cyclePosition = [-1] * len(edges)

        for start in range(len(edges)):
            if cycleNumber[start] != -1:
                continue

            pos = 0
            idx = start

            while idx != -1:
                if cycleNumber[idx] == -1:
                    cyclePosition[idx] = pos
                    cycleNumber[idx] = start
                    idx = edges[idx]
                    pos += 1
                elif cycleNumber[idx] == cycleNumber[start]:
                    res = max(res, pos - cyclePosition[idx])
                    break
                else:
                    break

        return res


        