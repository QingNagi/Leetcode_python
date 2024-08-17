# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        s = head
        f = head
        memo = []
        while f.next != None:
            memo.append(s.val)
            s = s.next
            f = f.next.next
            if f == None:
                break
        if f!= None and f.next == None:
            s = s.next
        while s != None:
            cur = memo.pop()
            if cur == s.val:
                s = s.next
            else:
                return False
        return True