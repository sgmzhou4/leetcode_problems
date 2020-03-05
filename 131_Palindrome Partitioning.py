'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def Check(s):
            if s == s[::-1]:
                return True
        
        def BackTracking(s, curr, res):
            if not s:                   # When the rest S is [], curr will be a valid solution
                res.append(curr)
            for i in range(1, len(s)+1):
                if Check(s[:i]):        # Check if the previous part is valid
                    BackTracking(s[i:], curr+[s[:i]], res)      # Go through the part left
        res = []
        BackTracking(s, [], res)
        return res