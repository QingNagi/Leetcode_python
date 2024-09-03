# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        low = head
        res = []
        while low: 
            res.append(low.val)
            low = low.next
        l, r = 0, len(res) - 1
        t_res = 0
        while l < r:
            t_res = max(t_res, res[l]+ res[r])
            l += 1
            r -= 1
        return t_res