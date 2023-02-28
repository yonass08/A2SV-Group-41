class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixes = [0]
        for num in nums:
            prefixes.append(prefixes[-1] + num)

        min_queue = deque([0])

        res = len(nums) + 1

        for i in range(1, len(prefixes)):
            while min_queue and prefixes[i] - prefixes[min_queue[0]] >= k:
                res = min(res, i - min_queue[0])
                min_queue.popleft()

            while min_queue and prefixes[i] <= prefixes[min_queue[-1]]:
                min_queue.pop()
            min_queue.append(i)

        return res if res <= len(nums) else -1

