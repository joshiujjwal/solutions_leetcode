class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs):
            rng = len(strs[0])
            for i in strs:
                rng = min(len(i),rng)
            
            for i in range(0,rng):
                res = strs[0][i]
                for j in strs:
                    if res == j[i]:
                        continue
                    return strs[0][:i]
            return strs[0][:rng]
                    
        else:
            return ""
