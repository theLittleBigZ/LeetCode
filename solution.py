# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        ret = None
        for ele in preorder:
            ret = self.insert(ret, ele)
        return ret
