class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        counter = [0] * len(persons)
        max_vote = 0
        curr_winner = 0

        self.winner_t = []
        self.times = []

        for i, person in enumerate(persons):
            counter[person] += 1

            if counter[person] >= max_vote:
                curr_winner = person
                max_vote = counter[person]

                self.winner_t.append(curr_winner)
                self.times.append(times[i])

    def q(self, t: int) -> int:
        low = 0
        high = len(self.times) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if self.times[mid] <= t:
                low = mid + 1
            else:
                high = mid - 1

        return self.winner_t[high]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
