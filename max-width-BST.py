# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([(root, 0)])

        while queue:
            length = len(queue)
            small = queue[0][1]
            large = 0

            for i in range(length):
                node, pos = queue.popleft()
                large = pos
                
                if node.left:
                    queue.append((node.left, 2 * pos))

                if node.right:
                    queue.append((node.right, 2 * pos + 1))

            res = max(res, large - small + 1)

        return res

        
