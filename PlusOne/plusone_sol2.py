class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        no = 0
        for i in range(0,n):
            no += digits[i] * 10**(n-i-1)
        no= no+1

        res = []
        
        while no>0:
            l = no%10
            no = no /10 
            res = [l] + res
        
        return res