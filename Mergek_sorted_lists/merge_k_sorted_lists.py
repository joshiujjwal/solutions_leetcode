# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        if(l1.val<=l2.val):
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)-1
        if l == -1:
            return None
        while l>0:
            i=0
            j=l
            
            while i<j:
                lists[i] = self.mergeTwoLists(lists[i],lists[j])
                i+=1
                j-=1
                
                if(i>=j):
                    l = j
                    
                    
        
        return lists[0]
            
        
    
        