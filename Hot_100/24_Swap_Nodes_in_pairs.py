# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        list1 = head
        cur = res = ListNode(next=head)
        while res.next and res.next.next:
            list1_next = list1.next.next
            temp = list1.next

            temp.next = list1
            res.next = temp
            res.next.next = list1
            res = res.next.next
            list1.next = list1_next
            list1 = list1_next
        return cur.next