class Solution(object):
    
    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b,a%b)


    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0,self.gcd(n,k)):
            temp = nums[n-k-i]
            j = i+k
            while 1:
                l = j + k
                if l <n:
                    l = l+k
                else:
                    break
                nums[l] = nums[j]
                j=l
            nums[j] = temp
                
                
        