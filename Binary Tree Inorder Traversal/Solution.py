# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if root:
            ret = ret + self.inorderTraversal(root.left)
            ret.append(root.val)
            ret = ret + self.inorderTraversal(root.right)
        return ret
