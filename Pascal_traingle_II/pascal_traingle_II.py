class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = []
        if rowIndex == 0:
             return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex > 1:
            n = self.getRow(rowIndex-1)
            l.append(1)
            for i in range(0,len(n)-1):
                l.append(n[i]+n[i+1])
            l.append(1)
            return l
                    