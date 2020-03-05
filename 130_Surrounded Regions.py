'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, 
which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        m = len(board)
        n = len(board[0])
        def DFS(x,y):
            if (x<0 or x>=n or y<0 or y>=m or board[y][x] != 'O'):
                return
            board[y][x] = 'G'       # find all 'O's at bounary and labeled as 'G'
            DFS(x,y-1)
            DFS(x-1,y)              # search around the 'O'
            DFS(x+1,y)
            DFS(x,y+1)
            
        for y in range(m):
            DFS(0,y)
            DFS(n-1,y)
        
        for x in range(n):
            DFS(x,0)
            DFS(x,m-1)
            
        h = {'G':'O', 'O':'X', 'X':'X'}
        
        for y in range(m):
            for x in range(n):
                board[y][x] = h[board[y][x]]
        
        return board