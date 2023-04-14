# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, parent, child):
            nonlocal res
            if root == None:
                return 

            if child:
                res += root.val

            n_parent = root.val % 2 == 0

            dfs(root.left, n_parent, parent)
            dfs(root.right, n_parent, parent)

        dfs(root, False, False)
        return res

            