# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(curr, head, tot):
            if head.left == None and head.right == None:
                if curr != [] and tot == targetSum:
                    res.append(curr.copy())
                return 

            if head.left:
                curr.append(head.left.val)
                dfs(curr, head.left, tot + head.left.val)
                curr.pop()

            if head.right:
                curr.append(head.right.val)
                dfs(curr, head.right, tot+head.right.val)
                curr.pop()

        dfs([root.val], root, root.val)
        return res