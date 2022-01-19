# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        visited = []
        val = []
        prev = None
        
        while head and head not in visited:
            visited.append(head)
            val.append(head.val)
            prev = head
            head = head.next
        
        if head == None:
            return None
        else:
            return visited[visited.index(head)]
            
