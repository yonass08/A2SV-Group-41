# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if root == None:
                return 0, 0

            left = helper(root.left)
            right = helper(root.right)

            return max(left) + max(right), root.val + left[0] + right[0]

        return max(helper(root))