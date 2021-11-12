# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            if cur.val == val:
                if head == cur:
                    head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head
