class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_total = nums[0]
        max_now = nums[0]
        for i in range(1,len(nums)):
            max_now = max(nums[i],max_now+nums[i])
            max_total = max(max_now,max_total)
            
        return max_total
