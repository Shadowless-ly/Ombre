class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        # if len(str(x)) < 1:
        #     return False
        # i = 0
        # j = len(str(x)) - 1
        # while i < j:
        #     if str(x)[i] == str(x)[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False
        # return True
        # print('Get:', x)
        # if x < 0:
        #     return False
        # if (x // 10) < 1:
        #     return True
        
        # ranger = 1
        # while x // ranger >= 10:
        #     ranger *= 10
        #     print('ranger', ranger)

        # left = x // ranger
        # print('left:', left)
        # right = x % 10
        # print('right:', right)
        # if left != right:
        #     return False
        # else:
        #     x -= left * ranger
        #     x //= 10
        #     print(x)
        #     if (x // 10) < 1:
        #         return True
        #     else:
        #         bo = self.isPalindrome(x)
        #         return bo


        tmp = x
        reverse = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        while tmp > 0:
            reverse = reverse * 10 + tmp % 10
            tmp //= 10
        return reverse == x

a = Solution()
print(a.isPalindrome(11111121))