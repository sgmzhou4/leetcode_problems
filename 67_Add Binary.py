'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)   # filled up with 0
        carry = 0
        res = ''
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry%2 == 1:    # if 1 left, append 1
                res += '1'
            else:
                res += '0'
            carry = carry//2    # carry return to the next iteration
        if carry == 1:
            res += '1'
        res = res[::-1]     #reverse the string
        return res