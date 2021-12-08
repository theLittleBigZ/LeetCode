# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def down(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.down(root.left)
        right = self.down(root.right)
        
        if left > right:
            return left + 1
        else:
            return right + 1
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.down(root.left)
        right = self.down(root.right)
        
        diaL = self.diameterOfBinaryTree(root.left)
        diaR = self.diameterOfBinaryTree(root.right)
        return max(left+right, max(diaL, diaR))
