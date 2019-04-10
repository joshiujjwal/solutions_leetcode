# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = headA
        l2 = headB
    
        c1 = 0
        c2 = 0
        
        while(l1):
            c1+=1
            l1=l1.next
        while(l2):
            c2+=1
            l2=l2.next
        
        if c1>=c2:
            d = c1-c2
        else:
            d = c2-c1
            headA,headB = headB,headA
        
        while(d):
            headA = headA.next
            d-=1
        
        while(headA is not None and headB is not None):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
                
        return None

        