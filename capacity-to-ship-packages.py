class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = (low + high) // 2

            if self.min_days(weights, mid) <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low




    def min_days(self, weights, capacity):
        count = 1
        curr_sum = 0

        for weight in weights:
            curr_sum += weight
            if curr_sum > capacity:
                count += 1
                curr_sum = weight

        return count
