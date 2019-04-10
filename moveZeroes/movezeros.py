class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c = 0
        for i in nums:
            if i!=0:
                nums[c] = i
                c+=1
                
        while(c<len(nums)):
            nums[c] = 0
            c+=1
    