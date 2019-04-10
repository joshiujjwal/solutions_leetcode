class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = []
        
        i = 0
        j = 0
        while i<len(s):
            while(ord(s[j])!=32):
                j+=1
                if j>=len(s):
                    break
                continue
            if i!=j:
                d = [str(s[i:j])] + d 
            i=j+1
            j+=1

            
        return ' '.join(d)
            