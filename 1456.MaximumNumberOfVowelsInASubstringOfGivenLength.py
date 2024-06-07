# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


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
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        currsum = maxsum = 0

        for i in range(len(s[:k])):
            if self.isVowel(s[i]):
                currsum += 1
                maxsum += 1
        
        for i in range(k, len(s)):
            if self.isVowel(s[i]):
                currsum += 1
            
            if not self.isVowel(s[i - k]):
                currsum -= 1

            maxsum = max(maxsum, currsum)

        return maxsum / k
    

s = "leetcode"
k = 3

myclass = Solution()
answer = myclass.maxVowels(s, k)
print(answer)