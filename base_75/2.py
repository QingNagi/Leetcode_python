# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = l1.val + l2.val
        next_1 = total//10
        root = res = ListNode(total%10)
        while l1.next and l2.next:
            total = l1.next.val + l2.next.val + next_1
            next_1 = total//10
            res.next = ListNode(total%10)
            l1, l2, res = l1.next, l2.next, res.next
        while l1.next:
            total = l1.next.val + next_1
            next_1 = total//10
            res.next = ListNode(total%10)
            l1, res = l1.next, res.next
        while l2.next:
            total = l2.next.val + next_1
            next_1 = total//10
            res.next = ListNode(total%10)
            l2, res = l2.next, res.next
        if next_1 != 0: res.next = ListNode(next_1)
        return root