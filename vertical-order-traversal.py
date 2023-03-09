# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_map = defaultdict(list)
        self.inorder(root, 0, 0, res_map)

        res = []

        for col in sorted(res_map):
            res.append([val for row, val in sorted(res_map[col])])

        return res
        

    def inorder(self, root, row, col, res_map):
        if root == None:
            return

        res_map[col].append((row, root.val))
        self.inorder(root.left, row+1, col-1, res_map)
        self.inorder(root.right, row+1, col+1, res_map)


