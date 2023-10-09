# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0

        prefixes = Counter([0])
        curr_sum = root.val

        return self.backtrack(prefixes, curr_sum, root, targetSum)


    def backtrack(self, prefixes, curr_sum, root, target):
        curr = curr_sum - target
        res = prefixes[curr]

        if root.left == None and root.right == None:
            return res
            
        prefixes[curr_sum] += 1

        if root.left:
            curr_sum += root.left.val
            res += self.backtrack(prefixes, curr_sum, root.left, target)
            curr_sum -= root.left.val
        
        if root.right:
            curr_sum += root.right.val
            res += self.backtrack(prefixes, curr_sum, root.right, target)
            curr_sum -= root.right.val

        prefixes[curr_sum] -= 1
        return res
        