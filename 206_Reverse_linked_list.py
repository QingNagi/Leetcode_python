# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        while(head != None and head.next != None):
            dummy_next = dummy.next
            temp = head.next
            dummy.next, head.next, temp.next = temp, temp.next, dummy_next
        return dummy.next