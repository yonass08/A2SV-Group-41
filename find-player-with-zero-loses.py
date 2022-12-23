class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCount = defaultdict(int)

        for winner, loser in matches:
            if not loseCount[winner]:
                loseCount[winner] = 0
            loseCount[loser] += 1
            
        zeroLoses = []
        oneLose = []

        for player in loseCount:
            if loseCount[player] == 0:
                zeroLoses.append(player)
            elif loseCount[player] == 1:
                oneLose.append(player)

        return [sorted(zeroLoses), sorted(oneLose)]
            
    
             
        
        

