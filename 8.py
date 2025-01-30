"""
Program to Check for Palindrome String
A string is said to be palindrome if the reverse of the string is the same as the string. In this article, we will learn how to check whether the given string is palindrome or not.
"""

class Solution:
    def palindrome1(self, s):
        if s == s[::-1]:
            return s + " is a palindrome"
        else:
            return s + " is not a palindrome"
# sol = Solution()
# print(sol.palindrome(s1)) #hello is not a palindrome
# print(sol.palindrome(s2)) #racecar is a palindrome
# print(sol.palindrome(s3)) #malayalam is a palindrome
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
s1 = "hello"
s2 = "racecar"
s3 = "malayalam"
class Solution:
    def palindrome2(self, s):
        if s == "".join(reversed(s)):
            return s + " is a palindrome"
        else:
            return s + " is not a palindrome"
sol = Solution()
print(sol.palindrome2(s1)) #hello is not a palindrome
print(sol.palindrome2(s2)) #racecar is a palindrome
print(sol.palindrome2(s3)) #malayalam is a palindrome
