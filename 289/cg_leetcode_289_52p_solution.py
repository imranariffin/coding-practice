class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        for r in range(m):
            for c in range(n):
                neighbor = 0
                
                for offset in [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]:
                    rn = r + offset[0]
                    cn = c + offset[1]
                    
                    if rn >= 0 and rn < m and cn >= 0 and cn < n:
                        if board[rn][cn] > 0:
                            neighbor += 1
                            
                if board[r][c] == 0:
                    if neighbor == 3:
                        board[r][c] = -1
                else:
                    if neighbor < 2:
                        board[r][c] = 2
                    elif neighbor == 2 or neighbor == 3:
                        board[r][c] = 3
                    else:
                        board[r][c] = 2
                        
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1 or board[r][c] == 1 or board[r][c] == 3:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
                    
        print(board)
        
        return
