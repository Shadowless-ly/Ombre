from functools import reduce
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbol_list = ['(', ')', '{', '}', '[', ']']
        err_list = ['(}', '(]', '{]', '{)', '[}', '[)']
        symbol_count = list(map(lambda x: s.count(x), symbol_list))
        if symbol_count[0] != symbol_count[1] or symbol_count[2] != symbol_count[3] or symbol_count[4] != symbol_count[5]:
            return False
        elif reduce(lambda m, n: m + n, map(lambda x: s.find(x) + 1, err_list)) > 0:
            return False
        else:
            return True

            