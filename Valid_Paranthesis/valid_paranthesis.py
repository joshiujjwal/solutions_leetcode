class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = {'(','{','['}
        end = {')','}',']'}
        l = []
        for i in s:
            if i in start:
                l.append(i)
            if i in end and len(l)==0:
                return False
            else:
                if i == ')':
                    if l[-1] == '(':
                        l.pop()
                    else:
                        return False
                if i == ']':
                    if l[-1] == '[':
                        l.pop()
                    else:
                        return False
                if i == '}':
                    if l[-1] == '{':
                        l.pop()
                    else:
                        return False
            
        if len(l) == 0:
            return True
        else:
            return False
