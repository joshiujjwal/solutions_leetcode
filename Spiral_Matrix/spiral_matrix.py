class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])
        i = 0
        j = 0
        while(i<m and j<n):
            for k in range(j,n):
                res.append(matrix[i][k])
            i+=1
            for k in range(i,m):
                res.append(matrix[k][n-1])
            n-=1
            if (i<m):
                for k in range(n-1,j-1,-1):
                    res.append(matrix[m-1][k])
                m-=1
            if (j<n):
                for k in range(m-1,i-1,-1):
                    res.append(matrix[k][j])
                j+=1
        return res