# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, 0, len(preorder))
        

    def helper(self, preorder, start, end):
        if start == end:
            return None

        root = TreeNode(preorder[start])
        right = bisect.bisect(preorder, preorder[start], start+1, end)
        root.left = self.helper(preorder, start+1, right)
        root.right = self.helper(preorder, right, end)

        return root


