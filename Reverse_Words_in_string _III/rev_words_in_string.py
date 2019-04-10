class Solution(object):
        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = 0
        while(i<len(s)):
            while(ord(s[j])!=32):
                j+=1
                if j>=len(s):
                    break
                continue
            s = s[0:i] + s[i:j][::-1] + s[j:]
            i = j+1
            j+=1
        
        return s