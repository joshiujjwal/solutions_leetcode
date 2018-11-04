class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        if x_str[0]=='-':
            r = x_str[1:]
            res= int(r[::-1])*(-1)
        else:
            res= int(x_str[::-1])
        if res>(2**31)-1 or res<-(2**31):
            return 0
        else:
            return res