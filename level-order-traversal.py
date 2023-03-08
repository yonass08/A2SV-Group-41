# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        next_level = []
        if root:
            next_level = [root]

        res = []

        while next_level:
            temp = []
            curr_level = []

            for node in next_level:
                curr_level.append(node.val)

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            res.append(curr_level)
            next_level = temp

        return res

        
