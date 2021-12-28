# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = []
        while head:
            val.append(head.val)
            head = head.next
        root = ListNode()
        temp = root
        for x in val[(len(val)//2):]:
            temp.next = ListNode(x)
            temp = temp.next
        return root.next
            
