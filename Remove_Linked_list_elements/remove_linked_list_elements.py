# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        curr = head
        while(curr.next):
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        
        return head if head.val!=val else head.next