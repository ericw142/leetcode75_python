# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"

# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

 

# Constraints:

#     1 <= s.length <= 3 * 105
#     s consist of printable ASCII characters.


class Solution(object):
    def isVowel(self, char):
        """
        :type char:str
        :rtype: bool
        """
        vowels = ['a','e','i','o','u']
        if char.lower() in vowels:
            return True
        else:
            return False

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        