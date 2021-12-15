# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head=head.next
        nums.sort()
        ret = ListNode()
        thing = ret
        for num in nums:
            temp = ListNode(num)
            thing.next = temp
            thing = thing.next
        return ret.next
