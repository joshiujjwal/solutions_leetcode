# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        m = len(A)
        n = len(B)
        res = []
        i = 0
        j = 0
        while(i<m and j<n):
            l = max(A[i].start,B[j].start)
            h = min(A[i].end,B[j].end)
            if l<=h:
                res.append(Interval(l,h))
                
            if(A[i].end < B[j].end):
                i+=1
            else:
                j+=1
                        
        return res