# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mode_count = 0


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        self.helper(root, counter)
        modes = []

        for num in counter:
            if counter[num] == self.mode_count:
                modes.append(num)

        return modes
        

    
    def helper(self, root, counter):
        if root == None:
            return

        counter[root.val] += 1
        if counter[root.val] >= self.mode_count:
            self.mode_count = counter[root.val]

        self.helper(root.left, counter)
        self.helper(root.right, counter)


        
