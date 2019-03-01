class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [True] * n
        
        count[0] = False
        count[1] = False
        
        i = 2
        while i*i<n:
            if not count[i]:
                i+=1
                continue
            j = i*i
            while(j<n):
                count[j] = False
                j += i
            i+=1

        return sum(count)