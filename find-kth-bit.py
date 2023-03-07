class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        mlist = ['0'] * k
        pivot = 0
        for i in range(1, k):
            if i == 2 * (pivot+1) - 1:
                mlist[i] = '1'
                pivot = i
            else:
                index = 2 * pivot - i
                mlist[i] = '1' if mlist[index] == '0' else '0'

        return mlist[-1]
