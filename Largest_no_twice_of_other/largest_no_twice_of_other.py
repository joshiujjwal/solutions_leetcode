class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_num = -sys.maxsize -1
        n = len(nums)
        for i in range(0,n):
            if nums[i] > max_num:
                max_num = nums[i]
        
        second_max_num = -sys.maxsize -1
        for i in range(0,n):
            if nums[i] < max_num and nums[i] > second_max_num:
                second_max_num = nums[i]
        
        if max_num >= 2 * second_max_num:
            return nums.index(max_num)
        else:
            return -1