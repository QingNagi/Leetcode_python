class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        self.plus_helper(dummy,0)
        if dummy.val == 0:
            return dummy.next
        return dummy
    def plus_helper(self,node,carry):
        if not node.next:
            if node.val < 9:
                node.val = node.val + 1
                return 0
            else:
                node.val = 0
                return 1
        else:
            carry = self.plus_helper(node.next,carry)
            new_val = (node.val + carry) % 10
            carry = (node.val + carry) // 10
            node.val = new_val
            return carry