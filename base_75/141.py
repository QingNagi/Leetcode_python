# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next: return False
        s = f = head
        while f:
            if not f.next or not f.next.next:
                return False
            else: f = f.next.next
            s = s.next
            if s == f: return True