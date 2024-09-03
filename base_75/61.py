# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0: return head
        dummy= res1 = ListNode(next=head)
        res = []
        root = head
        while root:
            res.append(root.val)
            root = root.next
        n = len(res)
        if k > n:
            k = k % n
        res[:k], res[k:] = res[n-k:], res[:n-k]
        for j in res:
            dummy.next = ListNode(j)
            dummy = dummy.next
        return res1.next