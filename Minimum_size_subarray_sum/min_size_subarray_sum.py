import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        j = 0
        r = sys.maxsize
        ms = 0
        for i, e in enumerate(nums):
            ms +=e
            while ms>=s:
                r = min(r,i-j+1)
                ms -= nums[j]
                j+=1
                
        if r == sys.maxsize:
            return 0
        else:
            return r