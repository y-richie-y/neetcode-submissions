# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# A -> B -> C
# A <- B <- C

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            new_head = head.next
            head.next = prev
            prev = head
            head = new_head
        return prev
        