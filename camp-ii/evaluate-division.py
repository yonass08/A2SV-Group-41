class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        existing = set()
        for var1, var2 in equations:
            existing.add(var1)
            existing.add(var2)

        graph = defaultdict(lambda : [[], []])

        for i in range(len(equations)):
            var1, var2 = equations[i]
            val = values[i]

            graph[var1][0].append(var2)
            graph[var1][1].append(val)

            graph[var2][0].append(var1)
            graph[var2][1].append(1 / val)


        res = []
        for var1, var2 in queries:
            if var1 not in existing or var2 not in existing:
                res.append(-1.0)
            else:
                res.append(self.calculateResult(var1, var2, graph, set()))

        return res
            

    def calculateResult(self, src, dest, graph, seen):
        for i in range(len(graph[src][0])):
            child = graph[src][0][i]
            val = graph[src][1][i]

            if child in seen:
                continue

            seen.add(child)
            if child == dest:
                return val

            res = self.calculateResult(child, dest, graph, seen)
            if res == -1.0:
                continue

            return val * res

        return -1.0
            

