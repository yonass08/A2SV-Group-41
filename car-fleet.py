class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort()
        fleet_count = 0
        
        time = 0
        for i in range(len(cars) - 1, -1, -1):
            current_time = (target - cars[i][0]) / cars[i][1]
            if current_time > time:
                fleet_count += 1
                time = current_time
            
        return fleet_count
        
