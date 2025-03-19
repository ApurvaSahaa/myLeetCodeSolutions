# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        n = 0
        while l.next != None:
            n += 1
            l = l.next
        n += 1
        l = head
        if n % 2 == 0:
            i = (n//2) + 1
            while i != 1:
                i -= 1
                l = l.next
        else:
            i = (n//2) + 1
            while i != 1:
                i -= 1
                l = l.next
        return l
