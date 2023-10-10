# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = Counter()
        res = []
        
        def countSub(root):
            if root == None:
                return "None"
            
            pre = str(root.val) + " " + countSub(root.left) + " " + countSub(root.right)
            if count[pre] == 1:
                res.append(root)
            count[pre] += 1
            
            return pre
    
        countSub(root)
        return res
            
            
        