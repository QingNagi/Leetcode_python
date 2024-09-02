# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        root = head
        while root:
            for _ in range(m-1):
                if root.next:
                    root = root.next
                else: return head
            if root.next:
                root_next = root.next
            else: return head
            for _ in range(n):
                if root_next.next:
                    root_next = root_next.next
                else: 
                    root_next = root_next.next
                    break
            root.next = root_next
            root = root.next
        return head