# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.helper(root, k)[1]
        

    def helper(self, root, k):
        if root == None:
            return [0, 0]

        left_count, left_num= self.helper(root.left, k)

        if k <= left_count:
            return [left_count, left_num]

        if k == left_count + 1:
            return [left_count + 1, root.val]

        right_count, right_num = self.helper(root.right, k-left_count-1)
        return [left_count + right_count + 1, right_num]
        
