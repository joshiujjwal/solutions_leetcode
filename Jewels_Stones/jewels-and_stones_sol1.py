class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0 
        l = [0] * 123
        for i in J:
            l[ord(i)] = 1
            
        for i in S:
            if l[ord(i)] == 1:
                count+=1
                
        return count
        
        
        
