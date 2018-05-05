#!/usr/bin/env python

# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ''
#         strs.sort(key=lambda x : len(x))
#         for s in range(len(strs[0])):
#             for i in strs[1:]:
#                 if len(i) < s+1:
#                     return i
#                 elif strs[0][s] != i[s]:
#                     return strs[0][:s]
#         return strs[0]


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

sol = Solution()
print(sol.longestCommonPrefix(["aa", "ab", "ac"]))

