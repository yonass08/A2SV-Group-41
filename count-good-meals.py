class Solution:
    def countPairsAddingTo(self, counter, powerOfTwo):
        """
        returns the number of pairs adding to the specific powerOfTwo passed as arguments
        """
        res = 0
        for deliciousness in counter:
            if 2 * deliciousness > powerOfTwo:
                continue
            if 2 * deliciousness == powerOfTwo:
                res += counter[deliciousness] * (counter[deliciousness]-1) // 2
            else:
                res += counter[deliciousness] * counter[powerOfTwo - deliciousness]
        
        return res


    def countPairs(self, deliciousness: List[int]) -> int:
        # Preprocessing
        mod = 10**9 + 7
        Max = 2*max(deliciousness)
        counter = Counter(deliciousness)

        res = 0
        powerOfTwo = 1

        while powerOfTwo <= Max:
            res += self.countPairsAddingTo(counter, powerOfTwo)
            res %= mod
            powerOfTwo *= 2

        return res
