class Solution:
    def is_safe(self, row, col, board, n):
        # check upper element
        duprow = row
        dupcol = col


        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1


        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1


        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1


        return True
    
    def solve(self, col, board, ans, n):
        if col == n:
            ans.append([''.join(row) for row in board])
            return
        
        for row in range(n):
            if self.is_safe(row, col, board, n):
                board[row][col] = 'Q'
                self.solve(col + 1, board, ans, n)
                board[row][col] = '.'
    
    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans

# Main function
def main():
    n = 4  # 4x4 grid and 4 queens
    obj = Solution()
    ans = obj.solveNQueens(n)
    
    for i, arrangement in enumerate(ans):
        print(f"Arrangement {i + 1}")
        for row in arrangement:
            print(row)
        print()

if __name__ == "__main__":
    main()
