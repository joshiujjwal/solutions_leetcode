class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(" ")
        for i in l[::-1]:
            if i!='':
                return len(i)
        return 0 
        
