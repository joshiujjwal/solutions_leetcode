class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(0,n+1):
            for j in range(0,math.ceil(n/2)+1):
                if i + 2*j == n:
                    count+=math.factorial(i+j)/(math.factorial(i)*math.factorial(j))
        
        
        return round(count)
