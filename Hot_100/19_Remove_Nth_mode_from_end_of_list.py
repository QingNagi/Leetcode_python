# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list1 = next=head
        counter_1 = 1
        list2 = dummy = ListNode(next=head)
        while list1:
            if counter_1 > n:
                list2 = list2.next 
            list1 = list1.next
            counter_1 += 1
        list2.next = list2.next.next
        return dummy.next