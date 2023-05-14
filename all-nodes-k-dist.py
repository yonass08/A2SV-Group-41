# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)

        queue = deque([target.val])
        seen = set([target.val])
        count = 0

        while queue and count < k:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for child in graph[curr]:
                    if child not in seen:
                        queue.append(child)
                        seen.add(child)
            count += 1

        return list(queue)
