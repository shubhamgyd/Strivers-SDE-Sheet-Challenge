def solution(col, row, board, n):
    duprow = row
    dupcol = col
    while(row >= 0 and col >= 0):
        if(board[row][col] == 'Q'):
            return False
        row -= 1
        col -= 1
    
    col = dupcol
    row = duprow
    while(col >= 0):
        if(board[row][col] == 'Q'):
            return False
        col -= 1
    
    row = duprow
    col = dupcol
    while(row < n and col >=0):
        if(board[row][col] == 'Q'):
            return False
        row += 1
        col -= 1
    
    return True

def NQueens(ind, board, ans, n):
    if(ind == n):
        temp = []
        for i in range(n):
            temp.append(board[i].copy())
        ans.append(temp)
        
        # ans.append([''.join(row) for row in board])
        # temp = [['.' for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         temp[i][j] = board[i][j]
        # ans.append(temp)
        return
    
    for i in range(n):
        if solution(ind,i,board,n):
            board[i][ind] = 'Q'
            NQueens(ind+1,board,ans,n)
            board[i][ind] = '.'

def printNQueens(n):
    board = []
    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    # temp = []
    # for i in range(n):
    #     temp.append('.')
    # for i in range(n):
    #     board.append(temp.copy())
    NQueens(0, board, ans, n)
    return ans

d = printNQueens(4)
for i in range(len(d)):
    for j in range(len(d[i])):
        print(d[i][j])
    print()