# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if node == None:
                return 0, 0
            
            nl, cl = dfs(node.left)
            nr, cr = dfs(node.right)
            
            res += abs(nl - cl)
            res += abs(nr - cr)
            
            return nl + nr + 1, cl + cr + node.val
        
        dfs(root)
        return res
        