# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        res = -1

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                parent = stack.pop()
                k -= 1

                if k == 0:
                    res = parent.val
                    break

                curr = parent.right

        return res
        