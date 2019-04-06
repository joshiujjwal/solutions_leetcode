class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ''
        
        i = len(a)-1
        j = len(b)-1
        
        while(i>=0 or j>=0 or carry==1):
            carry += int(a[i]) if i>=0 else 0
            carry += int(b[j]) if j>=0 else 0
            
            result = str( carry%2) + result
            
            carry/=2
            
            i-=1
            j-=1
        
        return result
            
            
        
        
            
            