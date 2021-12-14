# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def search(root,key):
            if root is None:
                return False
            elif root.val == key:
                return True
            
            if root.val < key:
                return search(root.right,key)
            return search(root.left,key)
        
        total = 0
        for x in range(low, high+1):
            if search(root, x):
                total += x
        return total
