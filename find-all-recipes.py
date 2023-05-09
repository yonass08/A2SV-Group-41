class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                indegree[recipes[i]] += 1

        queue = deque(supplies)
        seen = set(supplies)
        res = []

        while queue:
            curr = queue.popleft()
            if curr in indegree:
                res.append(curr)

            for child in graph[curr]:
                if child in seen:
                    continue
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    seen.add(child)

        return res





        
