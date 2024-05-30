# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_pos = 0
        subsequence = False
        if len(s) == 0:
            return True

        for t_pos in range(len(t)):
            if t[t_pos] == s[s_pos]:
                s_pos += 1
            if s_pos >= len(s):
                subsequence = True
                break

        return subsequence
        

s = "abc"
t = "ahbgdc"

myclass = Solution()
answer = myclass.isSubsequence(s, t)
print(answer)