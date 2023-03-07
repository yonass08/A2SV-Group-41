class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        if k == 2:
            return 1

        pivot = 2 ** int(math.log2(k))
        next_ = [[0, 1], [1, 0]]

        offset = (k - pivot - 1)
        return next_[self.kthGrammar(n, (pivot // 2) + (offset // 2) + 1)][offset % 2]

