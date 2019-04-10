# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        i=0
        carry = 0
        while(l1 or l2 or carry):
            r=carry
            r += l1.val if l1 else 0
            r += l2.val if l2 else 0
            
            if r >=10:
                carry = r // 10
                res.append(r%10)
            else:
                carry = 0
                res.append(r)
            i+=1
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
    
        
        l3 = ListNode(res[0])
        head = l3
        
        for i in range(1,len(res)):
            node = ListNode(res[i])
            l3.next = node
            l3 = l3.next
        
        
        return head