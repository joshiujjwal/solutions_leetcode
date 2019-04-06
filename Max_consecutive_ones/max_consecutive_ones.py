class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        tc = 0
        for i in nums:
            if i==1:
                tc+=1
                continue
            else:
                l = max(l,tc)
                tc=0
            
        l = max(l,tc)    
        return l