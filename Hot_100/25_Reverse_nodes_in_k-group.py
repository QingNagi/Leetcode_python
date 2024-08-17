class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        h = t = ListNode(0, head)
        p, stack = head, []        
        while True:
            for _ in range(k):
                if p: 
                    stack.append(p)   
                    p = p.next
                else: return h.next    
            for _ in range(k):
                t.next = stack.pop()   
                t = t.next
            t.next = p                 