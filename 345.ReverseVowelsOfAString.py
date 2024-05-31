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
        start = 0
        end = len(s) - 1

        s_array = list(s)

        while start < end:
            front_char = s_array[start]
            end_char = s_array[end]

            frontIsVowel = self.isVowel(front_char)
            endIsVowel = self.isVowel(end_char)

            if not frontIsVowel:
                start += 1
                continue
            if not self.isVowel(end_char):
                end -= 1
                continue
            if (frontIsVowel and endIsVowel):
                e = end_char
                s_array[end] = front_char
                s_array[start] = e

                start += 1
                end -= 1

        return ''.join(s_array)

            
        
s = "hello"

myclass = Solution()
answer = myclass.reverseVowels(s)
print(answer)