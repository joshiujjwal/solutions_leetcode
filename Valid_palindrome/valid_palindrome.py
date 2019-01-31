class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''
        
        for c in s:
            if re.match('^[a-zA-Z0-9_]+$',c):
                new_s += str(c).lower()
                
        i = 0
        j = len(new_s)-1
        while(i<j):
            if new_s[i] != new_s[j]:
                return False;
            i+=1
            j-=1
        
        return True
