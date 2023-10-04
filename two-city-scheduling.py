class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_a = sorted(costs, key = lambda x: x[0] - x[1])
        i = 0
        cost = 0
        while i < len(costs) //2:
            cost += cost_a[i][0]
            i += 1
        while i < len(costs):
            cost += cost_a[i][1]
            i += 1
        return cost