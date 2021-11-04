# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafy(self, root: Optional[TreeNode], left, leafs):
        if root:
            if root.left is None and root.right is None and left:
                leafs.append(root.val)
            self.leafy(root.left, True, leafs)
            self.leafy(root.right, False, leafs)
        return
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leafs = []
        self.leafy(root, False, leafs)
        x = 0
        for n in leafs:
            x = x + n
        return x
