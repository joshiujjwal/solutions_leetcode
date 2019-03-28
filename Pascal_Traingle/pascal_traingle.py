class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        if numRows <= 0:
            return []
        else:
            if numRows == 1:
                return res
            else:
                for i in range(1,numRows):
                    temp = []
                    temp.append(1)
                    for j in range(1,i):
                        temp.append(res[i-1][j-1]+res[i-1][j])
                    temp.append(1)  
                    res.append(temp)
            
        
        return res