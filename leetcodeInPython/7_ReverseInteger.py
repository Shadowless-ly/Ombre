class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        signed = -1 if x < 0 else 1
        num = signed*int(''.join((str(abs(x))[::-1])))
        return num if num<2**31 and num>-2**31 else 0
        

sol = Solution()
print(sol.reverse(-123))
print(2**31)
