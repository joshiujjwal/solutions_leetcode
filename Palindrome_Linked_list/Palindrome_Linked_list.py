# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        i = head
        j = head.next
        jhead = j
        
        while(j != None and j.next !=None):
            i.next = j.next
            i = i.next
            j.next = i.next
            j = j.next
            
        
        i.next = jhead
        
        return head