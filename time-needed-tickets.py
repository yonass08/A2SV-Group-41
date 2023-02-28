class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        mTicket = tickets[k]

        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], mTicket)
            else:
                res += min(tickets[i], mTicket-1)

        return res
