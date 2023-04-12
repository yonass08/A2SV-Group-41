# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root.left == None and root.right == None:
            return str(root.val)
        if root.left == None and root.right != None:
            return str(root.val) + '()(' + self.tree2str(root.right) + ')'
        if root.left != None and root.right == None:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'

        return str(root.val) + '(' + self.tree2str(root.left) + ')'  + '(' + self.tree2str(root.right) + ')'     
