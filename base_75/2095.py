# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:  return 
        fast = low = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else: 
                break
            if not fast or not fast.next :
                break
            else: low = low.next
        if low.next:  low.next = low.next.next
        else:  low.next = ListNode(None)
        return head