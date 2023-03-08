# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return self.are_mirror_flips(root.left, root.right)
        

    def are_mirror_flips(self, root1, root2):
        if root1 == None and root2 == None:
            return True

        if (root1 and root2 == None) or (root2 and root1 == None):
            return False

        if root1.val != root2.val:
            return False

        res1 = self.are_mirror_flips(root1.left, root2.right)
        res2 = self.are_mirror_flips(root1.right, root2.left)

        return res1 and res2
