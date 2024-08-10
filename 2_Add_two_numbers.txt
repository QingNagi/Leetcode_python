# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = l1.val + l2.val
        next = total//10
        res = ListNode(total%10)
        if l1.next != None or l2.next != None or next != 0:

            if l1.next != None:
                l1 = l1.next
            else:
                l1 = ListNode(0)

            if l2.next != None:
                l2 = l2.next
            else:
                l2 = ListNode(0)

            l1.val = l1.val + next

            res.next = self.addTwoNumbers(l1, l2)
        return res

        




