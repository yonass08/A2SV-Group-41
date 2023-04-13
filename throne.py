class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.dead = set()       
        self.kingName = kingName
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        res = []
        for name in self.preorder(self.kingName):
            if name not in self.dead:
                res.append(name)

        return res


    def preorder(self, root):
        res = [root]

        for child in self.graph[root]:
            res += self.preorder(child)

        return res

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()