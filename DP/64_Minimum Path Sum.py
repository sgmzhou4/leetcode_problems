'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1,m):        # case 1: j == 0 and i != 0
            grid[i][0] += grid[i-1][0]
        for i in range(1,n):        # case 2: i == 0 and j != 0
            grid[0][i] += grid[0][i-1]
        for i in range(1,m):        # case 3: i != 0 and j != 0
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            
        return grid[-1][-1]