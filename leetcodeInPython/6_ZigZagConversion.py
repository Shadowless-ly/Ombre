class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0:
            return None
        elif numRows == 1:
            return s
        
        li = []
        for i in range(numRows):
            print(range(numRows))
            i = i + 1
            new_li = []
            if (i == 1) or (i == numRows):
                j = i - 1
                while j <= len(s) - 1:
                    new_li.append(s[j])
                    j = j + 2* numRows -2
            else:
                j = i - 1
                head = j
                if head <= len(s)-1:
                    new_li.append(s[head])
                while j <= len(s)-1:
                    head = j
                    tail = head + 2* numRows - 2
                    middle = 2 * (numRows-i)+ j
                    print('head:', head, 'middle:', middle, "tail:", tail, 'i:', i-1, 'length:', len(s))
                    if middle <= len(s)-1:
                        print('add')
                        new_li.append(s[middle])
                        if tail <=len(s)-1:
                            new_li.append(s[tail])
                    j = tail
            li.append(new_li)
        print(li)
        return ''.join([n for n in [''.join(m) for m in li]])

#
# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows == 1 or numRows >= len(s):
#             return s

#         L = [''] * numRows
#         index, step = 0, 1

#         for x in s:
#             L[index] += x
#             if index == 0:
#                 step = 1
#             elif index == numRows -1:
#                 step = -1
#             index += step

#         return ''.join(L)
#


sol = Solution()
sol.convert("a", 4)