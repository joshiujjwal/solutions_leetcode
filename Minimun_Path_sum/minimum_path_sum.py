class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = grid
        
        
        i,j = 1,1
        while(i<n):
            grid[0][i] = grid[0][i]+grid[0][i-1]
            i+=1
            
        while(j<m):   
            grid[j][0] = grid[j][0]+grid[j-1][0]
            j+=1
        

            
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
                
        return grid[m-1][n-1]
                