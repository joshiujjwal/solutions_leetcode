"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            head = Node(insertVal)
            return head
        
        
        
        l = head

        while(l):
            a,b = l.val,l.next.val
            if ( a>b and (insertVal<=b or insertVal>=a) or (a<=insertVal<=b) or l.next == head):
                node = Node(insertVal)
                node.next = l.next
                l.next = node
                break
            
            l = l.next
                
        
        
        
        return head
    
        