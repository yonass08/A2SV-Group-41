class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        curr_sum = 0
        total_sum = 0
        min_stack = [-1]

        for idx, num in enumerate(arr):
            while len(min_stack) > 1 and num <= arr[min_stack[-1]]:
                last = min_stack.pop()
                curr_sum -= (last - min_stack[-1]) * (arr[last] - num)

            curr_sum += num
            min_stack.append(idx)
            total_sum = (total_sum + curr_sum) % (10**9+7)

        return total_sum
        
