class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n:
            res = nums[0]
            for i in range(1,n):
                res = res ^ nums[i]
            
            return res
        
                
        
    
                