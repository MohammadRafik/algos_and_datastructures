# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        head_saver = head
        len = 0
        while head:
            len += 1
            head = head.next
        
        middle = (len//2)
            
        head = head_saver
        for i in range(middle):
            head = head.next
        return head
            