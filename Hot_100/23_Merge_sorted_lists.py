# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:return 
        queue=[]
        for l in lists:#将lists的值放进小根堆
            head=l
            while head:
                heapq.heappush(queue,head.val)
                head=head.next
        dummy=ListNode(0)#构造虚拟节点
        cur=dummy
        while queue:#将堆顶取出连接成链表
            cur.next=ListNode(heapq.heappop(queue))
            cur=cur.next
        return dummy.next