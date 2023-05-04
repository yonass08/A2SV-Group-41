class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [[] for _ in range(len(parent))]

        for child in range(1, len(parent)):
            self.children[parent[child]].append(child)

        self.locked = [0] * len(parent)
        

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False

        self.locked[num] = user
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
            
        self.locked[num] = 0
        return True
        

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False

        if self.has_locked_ancestor(num):
            return False

        if not self.has_locked_descendant(num):
            return False

        self.locked[num] = user
        return True

    def has_locked_ancestor(self, num):
        while num >= 0:
            if self.locked[num] != 0:
                return True
            num = self.parent[num]

        return False

    def has_locked_descendant(self, num):
        temp = self.locked[num]
        self.locked[num] = 0
        res = False

        def dfs(node):
            nonlocal res
            if self.locked[node] != 0:
                res = True

            self.locked[node] = 0

            for child in self.children[node]:
                dfs(child)

        dfs(num)
        self.locked[num] = temp
        return res

        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)