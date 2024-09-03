# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        root = l= ListNode(-inf, next=head)
        temp = root
        while root and root.next:
            if root.val == root.next.val:
                while root.next and root.val == root.next.val:
                    root = root.next
                temp.next = root.next
                root = root.next
                continue
            temp = root
            root = root.next
        return l.next