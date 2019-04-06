class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)
        
        if(n == 0):
            return 0
        if (h >= n):
            ch = needle[0]
            for i in range(0,h):
                if ch == haystack[i]:              
                    if haystack[i:i+n] == needle:
                        return i
        
        
        return -1
                