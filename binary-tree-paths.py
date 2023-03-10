# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        curr = [str(root.val)]
        self.backtrack(root, curr, paths)
        res = []
        for path in paths:
            res.append('->'.join(path))
        return res



    def backtrack(self, root, curr, paths): 
        if root.left == None and root.right == None:
            paths.append(list(curr))
            return

        if root.left:
            curr.append(str(root.left.val))
            self.backtrack(root.left, curr, paths)
            curr.pop()

        if root.right:
            curr.append(str(root.right.val))
            self.backtrack(root.right, curr, paths)
            curr.pop()


        
