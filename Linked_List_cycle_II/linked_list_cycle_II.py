# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        i = 0
        curr = head
        while curr and curr.next:
            if curr in d.keys():
                return curr
            else:
                d[curr] = i
                i+=1
                curr=curr.next
                
            
        return None
                
            
        