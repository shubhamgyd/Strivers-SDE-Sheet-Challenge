class Solution:
    def isSafe1(self, row, col, board, n):
        # check in upper diagonal
        duprow = row
        dupcol = col
        
        
        while (row >= 0 and col >= 0):
            if(board[row][col] == 'Q'): 
                return False
            row -= 1
            col -= 1
        
        # check in the left
        col = dupcol
        row = duprow
        
        while (col >= 0):
            if(board[row][col] == 'Q'): 
                return False
            col -= 1
    
        
        # check in lower diagonal
        col = dupcol
        row = duprow
        
        while (row < n and col >= 0):
            if(board[row][col] == 'Q'): 
                return False
            row += 1
            col -= 1
        return True
    
    def solve(self, col, board, ans, n):
        if (col == n):
            temp = []
            for i in range(n):
                temp.append(board[i].copy())
            ans.append(temp)
            return
            
        for i in range(n):
            if self.isSafe1(i,col,board,n):
                board[i][col] = 'Q'
                self.solve(col+1,board,ans,n)
                board[i][col] = '.'

    def solveQueens(self, n):
        ans = []
        board = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(0,board,ans,n)
        return ans
    
if __name__=="__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        obj = Solution()
        d = obj.solveQueens(n)
        for j in range(len(d)):
            for k in range(len(d[j])):
                print(f"{d[j][k]}")
            print()