class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        i=0
        curr_max = 0
        total_max = 0
        while(i < len(s)):
            if  d.get(s[i],0) == 0:
                curr_max+=1
                d[s[i]] = i+1
                i+=1
            else:
                i = d[s[i]]
                curr_max = 0
                d = {}
            if curr_max > total_max:
                total_max = curr_max
        return total_max
        
        
