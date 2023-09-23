def solve(board):
    for i in range(9):
        for j in range(9):
            
            if board[i][j] == '.':
                for c in range(1,10):
                    if isPerfect(c,i,j,board):
                        board[i][j] = c
                        if(solve(board) == True):
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True
    

def isPerfect(c,row, col, board):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
            return False
    return True

def sudokuSolver(n):
    board = [['.' for i in range(9)] for i in range(9)]
    solve(board)
    for i in range(9):
        print(board[i])
sudokuSolver(9)