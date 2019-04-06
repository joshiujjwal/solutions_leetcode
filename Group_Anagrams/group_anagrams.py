class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        
        for i in strs:
            char_arr = [0] * 26
            for j in i:
                char_arr[ord(j)-97] +=1
            s =''
            for k in char_arr:
                s+=str(k)
            if s not in d.keys():
                d[s] = [i]
            else:
                d[s].append(i)
        
        res = []
        for i in d.keys():
            res.append(d[i])
        
        
        return res