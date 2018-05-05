#!/usr/bin/env python
from functools import reduce
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Sol one
        # M = ["", "M", "MM", "MMM"];
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        # return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]

        # Sol Two
        roman_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        roman_num = []
        num_list = reversed([1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000])
        get = lambda num, symbol : num // symbol * roman_dict[symbol]
        for symbol in num_list:
            roman_num.append(get(num, symbol))
            num = num % symbol

        return ''.join(roman_num)

        # Sol Three
        # 使用[1],4,[5],9,[10]去推所有数字的罗马数字组合

if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(1))