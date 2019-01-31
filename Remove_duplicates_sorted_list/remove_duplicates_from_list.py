# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = head
        if i is not None:
            j = head.next
            while(j is not None):
                if j.val == i.val:
                    i.next = j.next
                    j.next = None
                    j = i.next
                else:
                    i = i.next
                    j = j.next

                    
        return head
