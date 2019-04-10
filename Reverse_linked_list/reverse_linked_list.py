# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        i = head
        j =  i.next
        while(j is not None):
            h = ListNode(j.val)
            i.next = j.next
            h.next = head
            head = h
            j = j.next
        
        return head
        