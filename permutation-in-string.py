class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = Counter(s1)
        to_match = len(counter)

        for idx in range(len(s2)):
            counter[s2[idx]] -= 1
            if counter[s2[idx]] == 0:
                to_match -= 1

            if idx >= len(s1)-1:
                if to_match == 0:
                    return True

                counter[s2[idx-len(s1)+1]] += 1
                if counter[s2[idx-len(s1)+1]] == 1:
                    to_match += 1

        return False
