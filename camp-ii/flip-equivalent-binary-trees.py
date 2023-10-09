# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True
        
        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        straight =  self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        
        flip =  self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        
        return straight or flip
        