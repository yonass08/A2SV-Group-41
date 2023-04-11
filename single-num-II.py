class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        oneMod = 0
        twoMod = 0
        for num in nums:
            oneMod = (oneMod ^ num) & (~twoMod)
            twoMod = (twoMod ^ num) & (~oneMod)

        return oneMod