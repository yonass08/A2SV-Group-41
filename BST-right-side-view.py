# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root, 0)
        return self.res

    def helper(self, root, level):
        if root == None:
            return 

        if level == len(self.res):
            self.res.append(root.val)

        self.helper(root.right, level + 1)
        self.helper(root.left, level + 1)
