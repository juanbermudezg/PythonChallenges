'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Created by Juan Bermudez, backend developer
'''
class Solution(object):
    def romanToInt(self, s):
        s=s+' '
        number=0
        i=0
        while i< len(s):
            if (s[i]=='I'):
                if (s[i+1]=='V'):
                    number=number+4
                    i=i+2
                elif (s[i+1]=='X'):
                    number=number+9
                    i=i+2
                else:
                    number=number+1
                    i=i+1
            elif(s[i]=='V'):
                number=number+5
                i=i+1
            elif(s[i]=='X'):
                if (s[i+1]=='L'):
                    number=number+40
                    i=i+2
                elif (s[i+1]=='C'):
                    number=number+90
                    i=i+2
                else:
                    number=number+10
                    i=i+1
            elif(s[i]=='L'):
                number=number+50
                i=i+1
            elif(s[i]=='C'):
                if (s[i+1]=='D'):
                    number=number+400
                    i=i+2
                elif (s[i+1]=='M'):
                    number=number+900
                    i=i+2
                else:
                    number=number+100
                    i=i+1
            elif(s[i]=='D'):
                number=number+500
                i=i+1
            elif(s[i]=='M'):
                number=number+1000
                i=i+1
            else:
                i=i+1
        return number
