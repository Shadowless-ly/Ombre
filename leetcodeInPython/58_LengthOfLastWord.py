class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        for s in s.split()[::-1]:
            if s.isalpha:
                return len(s)
        return 0
