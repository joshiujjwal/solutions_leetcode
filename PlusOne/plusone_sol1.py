class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        j = 0
        n = 0
        while(j<len(digits)):
            n+=digits[j]*(10**(i-j))
            j=j+1
        n = n+1
        l = []
        j=0
        while(n):
            l.insert(0,n%10)
            n = n//10
            j=j+1
        return l
