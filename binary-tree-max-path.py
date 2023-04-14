# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def maxPath(root):
            nonlocal res
            if root == None:
                return 0

            left = max(maxPath(root.left), 0)
            right = max(maxPath(root.right), 0)

            res = max(res, left + root.val + right)
            return max(left, right) + root.val

        maxPath(root)
        return res