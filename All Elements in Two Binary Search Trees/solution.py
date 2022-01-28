# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        ret = []
        
        if root is None:
            return
        
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            ret.append(queue[0].val)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return ret
                
                
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.bfs(root1)
        l2 = self.bfs(root2)
        if l1 and l2:
            ret = l1+l2
            ret.sort()
            return ret
        else:
            if l1:
                l1.sort()
                return l1
            elif l2:
                l2.sort()
                return l2
            else:
                return []
