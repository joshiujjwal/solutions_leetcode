class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_sum = 0 
        r_sum = sum(nums)
        n = len(nums)
        
        for i in range(0,n):
            r_sum -= nums[i]
            if l_sum==r_sum:
                return i
            l_sum += nums[i]
        
        return -1