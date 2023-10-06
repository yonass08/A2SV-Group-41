class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(dishIndex, time):
            if dishIndex == len(satisfaction):
                return 0

            return max((satisfaction[dishIndex] * time) + dp(dishIndex+1, time+1),
                      dp(dishIndex+1, time))
            
        
        return dp(0, 1)
        