# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, curr):
            nonlocal res
            curr = curr * 10 + root.val
    
            if root.left == None and root.right == None:
                res += curr
                return 

            if root.left:
                dfs(root.left, curr)
            if root.right:    
                dfs(root.right, curr)

        dfs(root, 0)
        return res
