# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        
        def dfs(root, p, q):
            nonlocal res
            if root == None:
                return 
            
            val = False  
            if root == p or root == q:
                val = True
                
            if dfs(root.left, p, q):
                if val:
                    res = root
                val = True
                    
            if res:
                return
            
            if dfs(root.right, p, q):
                if val:
                    res = root
                val = True
                    
            return val
        
        dfs(root, p, q)
        return res
            
                
            

