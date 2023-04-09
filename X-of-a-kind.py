class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)

        curr = counter[deck[0]]
        for num in counter:
            curr = gcd(curr, counter[num])

        return curr != 1
