class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        for k in range(0,m+n):
            if k%2 == 0:
                if  k < m:
                    i = k
                    j = 0
                else:
                    i = m-1
                    j = k-(m-1)
                while(j < n and i >= 0):
                    res.append(matrix[i][j])
                    i-=1
                    j+=1
            else:
                if  k < n:
                    i = 0
                    j = k
                else:
                    i = k-(n-1)
                    j = n-1
                while(i < m and j >= 0 ):
                    res.append(matrix[i][j])
                    i+=1
                    j-=1
        return res