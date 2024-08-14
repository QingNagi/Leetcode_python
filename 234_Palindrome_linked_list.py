# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        stack = []
        temp = head
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        while len(stack) != 0  and head is not None:
            if stack.pop() != head.val:
                return False
            head = head.next
        return True