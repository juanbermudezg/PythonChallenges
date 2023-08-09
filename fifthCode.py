'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Created by Juan Bermudez, backend developer
'''
class Solution(object):
    def reverse(self, x):
        if x<0:
            number = str(x*-1)[::-1]
            number = '-'+number
        else:
            number = str(x)[::-1]
        if int(number)>=-(2**31) and int(number)<=(2**31)-1:
            return int(number)
        else:
            return 0
