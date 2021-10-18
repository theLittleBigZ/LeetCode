# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, par, dep, val):
            if not node: return
            if node.val == val: return dep, par
            return self.dfs(node.left, node, dep + 1, val) or self.dfs(node.right, node, dep + 1, val)
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        dep_x, par_x = self.dfs(root, None, 0, x)
        dep_y, par_y = self.dfs(root, None, 0, y)

        return dep_x == dep_y and par_x != par_y
