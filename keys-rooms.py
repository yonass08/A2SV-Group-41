class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])

        while queue:
            node = queue.popleft()
            visited.add(node)

            for child in rooms[node]:
                if child not in visited:
                    queue.append(child)

        return len(visited) == len(rooms)
