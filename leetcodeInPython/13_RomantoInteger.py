from functools import reduce
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = list(s)
        self.roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        self.symbol()
        return reduce(lambda x, y : x +y, self.num_list)

    def symbol(self):
        self.num_list = []
        for i in range(len(self.s)):
        	romannum = self.s.pop(0)
        	for i in self.s:
        		if self.roman_dict[romannum] < self.roman_dict[i]:
        			self.num_list.append(-self.roman_dict[romannum])
        			break
        	else:
        		self.num_list.append(self.roman_dict[romannum])


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt('IX'))