class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not (haystack or needle)) or (haystack and not needle):
            return 0

        sublenth = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+sublenth] == needle:
                    return i
        return -1


        # return haystack.find(needle)