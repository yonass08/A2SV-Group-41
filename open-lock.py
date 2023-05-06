class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dirns = ["1000", "9000", "0100", "0900", "0010", "0090", "0001", "0009"]

        def add(lock1, lock2):
            res = []
            for i in range(4):
                digit = (int(lock1[i]) + int(lock2[i])) % 10
                res.append(str(digit))
            return "".join(res)

        dead = set(deadends)
        if "0000" in dead:
            return -1 

        queue = deque(["0000"])
        visited = set(["0000"])

        res = -1
        while queue:
            res += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return res
                for dirn in dirns:
                    nlock = add(curr, dirn)
                    if nlock not in visited and nlock not in dead:
                        queue.append(nlock)
                        visited.add(nlock)

        return -1