class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = sorted(zip(growTime, plantTime), reverse = True)

        res = 0
        curr_sum = 0

        for grow_time, plant_time in plants:
            curr_sum += plant_time
            res = max(res, grow_time + curr_sum)

        return res
