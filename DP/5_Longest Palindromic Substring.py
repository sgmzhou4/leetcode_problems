'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        def getLen(l,r):
            while l >= 0 and r < length and s[l] == s[r]:   # if (c[i-1, j+1] is True && s[i] == s[j]) ==> c[i,j] is true
                l -= 1
                r += 1
            return r - l - 1    # In this case, the last s[l] != s[r] ==> only count l-1 and r-1
        start = 0
        max_len = 0
        for i in range(length):
            curr_len = max(getLen(i,i), getLen(i, i+1)) # when the center is a number or not 
            # exp:
            # [abcba] center is c
            # [abba] center is between b
            if curr_len <= max_len: continue
            max_len = curr_len
            start = i - (curr_len - 1)//2   # get the start index of the palindrome
            
        return s[start:start+max_len]