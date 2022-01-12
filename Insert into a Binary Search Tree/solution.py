# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ret = root
        if not root:
            return TreeNode(val)
        pre = root
        while root:
            pre = root
            if root.val < val:
                root = root.right
            else:
                root = root.left
        if pre.val < val:
            pre.right = TreeNode(val)
        else:
            pre.left = TreeNode(val)
        return ret
