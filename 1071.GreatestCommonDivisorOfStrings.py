# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

 

# Constraints:

#     1 <= str1.length, str2.length <= 1000
#     str1 and str2 consist of English uppercase letters.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1)<=len(str2):
            temp = str1
        else:
            temp = str2
        m = len(temp)
        x = 1
        gcd=[""]
        while x<=m:
            if m%x==0 and temp[:x] * (len(str1)//x) == str1 and temp[:x] * (len(str2)//x) == str2:
                gcd.append(temp[:x])
            x+=1
        return gcd[-1]
        
myclass = Solution()
answer = myclass.gcdOfStrings("ABABAB", "ABAB")
print(answer)