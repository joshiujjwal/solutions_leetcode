class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i=0
        j=0
        n1=0
        n2=0
        while(l1):
            n1 = n1 + (l1.val)*(10**i)
            i+=1
            l1=l1.next
        while(l2):
            n2 = n2 + (l2.val)*(10**j)
            j+=1
            l2=l2.next
            
        n = n1+n2
        print(n1,n2)
        l3 = ListNode(n%10)
        l4 = l3
        n = n//10
        while(n>0):
            temp = ListNode(n%10)
            l3.next = temp
            l3 = l3.next
            n = n//10
        
        return l4
