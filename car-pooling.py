class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 1001

        for num_passengers, start, end in trips:
            locations[start] += num_passengers
            locations[end] -= num_passengers

        r_sum = 0
        for num in locations:
            r_sum += num
            if r_sum > capacity:
                return False

        return True

        
