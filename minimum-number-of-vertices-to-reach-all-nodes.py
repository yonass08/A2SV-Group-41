class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        not_ans = set()

        for start, end in edges:
            not_ans.add(end)

        return filter(lambda x: x not in not_ans, list(range(n)))