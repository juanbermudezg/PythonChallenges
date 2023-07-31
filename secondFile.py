'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Created by Juan Bermudez, backend developer
'''
class Solution(object):
    def isPalindrome(self, x):
       num=''
       if x>=0:
            for i in range (len(str(x))-1,-1,-1):
               num=num+str(x)[i]
            if (num==str(x)):
                return True
            else:
               return False
       else:
           return False
