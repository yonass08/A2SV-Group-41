# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[0]

    def helper(self, root):
        if root == None:
            return [0, 0, 0]

        res1, sum1, count1 = self.helper(root.left)
        res2, sum2, count2 = self.helper(root.right)

        curr_sum = sum1 + sum2 + root.val
        curr_count = count1 + count2 + 1
        res = res1 + res2

        if curr_sum // curr_count == root.val:
            res += 1

        return [res, curr_sum, curr_count]
