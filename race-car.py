class Solution:
    def racecar(self, target: int) -> int:
        res = 0
        seen = set()

        queue = deque([(0, 1)])
        seen.add((0, 1))

        while queue:
            for i in range(len(queue)):
                pos, speed = queue.popleft()

                if pos == target:
                    return res

                A = (pos + speed, speed * 2)
                R = (pos, -1 if speed >= 0 else 1)

                if A not in seen:
                    queue.append(A)
                    seen.add(A)

                if R not in seen:
                    queue.append(R)
                    seen.add(R)
            res += 1

        return -1

                