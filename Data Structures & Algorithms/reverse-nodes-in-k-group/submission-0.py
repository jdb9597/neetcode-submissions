# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        group_head = head
        group_prev = dummy
        prev = dummy
        curr = head
        count = head
        while True:
            for i in range(k):
                if count is None:
                    return dummy.next
                group_tail = count
                count = count.next
            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            group_prev.next = group_tail
            group_head.next = curr
            group_prev = group_head
            prev = group_head
            group_head = curr
            count = curr




        
        