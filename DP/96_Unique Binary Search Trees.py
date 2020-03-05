'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

"""
when n = 4:

if root = 1:    left 0; right 3 ==> left ways: 1; right ways: 5 ===> total ways: 1*5
if root = 2:    left 1; right 2 ==> left ways: 1; right ways: 2 ===> total ways: 1*2
if root = 3:    left 2; right 1 ==> left ways: 2; right ways: 1 ===> total ways: 2*1
if root = 4:    left 3; right 0 ==> left ways: 5; right ways: 1 ===> total ways: 5*1

total ways: 5+2+2+5 = 14
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]*(n+1)
        res[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                res[i] += res[j]*res[i-j-1] # left ways * right ways
        
        return res[-1]