class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                tens += 1
                if fives == 0:
                    return False
                fives -= 1
            if bill == 20:
                if fives == 0:
                    return False
                fives -= 1

                if tens > 0:
                    tens -= 1
                elif fives > 1:
                    fives -= 2
                else:
                    return False

        return True


