class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n= len(s)
        i=0
        ans = [0]* (n+1)
        ans[0]=1
        for i in range(n):
            if ans[i]:
                for j in wordDict:
                    l=len(j)
                    if i+l <=n:
                        if s[i:i+l] == j:
                            ans[i+l] = 1
                                                

        if ans[-1]:
            return True
        else:
            return False
            
        