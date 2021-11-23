# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif(key > root.val):
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None and root.right is None:
              return None
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        succParent = root
        succ = root.right
        while succ.left != None:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
        root.val = succ.val

        return root
