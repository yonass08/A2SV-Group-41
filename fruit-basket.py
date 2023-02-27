class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        slow = 0
        maxCount = 0
        
        for fast in range(len(fruits)):
            basket[fruits[fast]] = basket.get(fruits[fast], 0) + 1
            
            if len(basket) > 2:
                basket[fruits[slow]] -= 1
                if basket[fruits[slow]] == 0:
                    del basket[fruits[slow]]
                slow += 1
            
        return fast - slow + 1
