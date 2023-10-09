class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        closestDist = [float('inf')] * len(houses)
        heaters.sort()
        houses.sort()

        heaterIdx = 0

        for i in range(len(houses)):
            while heaterIdx < len(heaters) and heaters[heaterIdx] < houses[i]:
                heaterIdx += 1
            
            if heaterIdx < len(heaters):
                closestDist[i] = min(closestDist[i], heaters[heaterIdx] - houses[i])

        heaterIdx = len(heaters) - 1
        for i in range(len(houses)-1, -1, -1):
            while heaterIdx >= 0 and heaters[heaterIdx] > houses[i]:
                heaterIdx -= 1
            if heaterIdx >= 0:
                closestDist[i] = min(closestDist[i], houses[i] - heaters[heaterIdx])

        # print(closestDist)

        return max(closestDist)

