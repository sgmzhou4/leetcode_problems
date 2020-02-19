'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

"""
TIPS:

P     I    N             PIN
A   L S  I G  ========>  ALSIG
Y A   H R                YAHR
P     I                  PI

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows == len(s):
            return s
        
        mat = ['' for i in range(numRows)]
        row = 0
        step = 1
        for i in s:
            mat[row] += i
            
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        
        mat = ''.join(mat)
        return mat