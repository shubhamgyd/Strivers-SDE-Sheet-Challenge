def spirallyTraverse(matrix, r, c):
    left = 0
    right = c
    top = 0
    bottom = r
    ans = []
    while (left <= right and top <=bottom):
        for i in range(left, right+1):
            ans.append(matrix[top][i])
            
        for i in range(top+1,bottom+1):
            ans.append(matrix[i][right])
        
        for i in range(right-1,left-1,-1):
            ans.append(matrix[bottom][i])
        
        for i in range(bottom-1,top,-1):
            ans.append(matrix[i][left])
        top = top + 1
        bottom = bottom - 1
        left = left + 1
        right = right - 1
    print(ans)
    # for i in range(right-1,left-1):
        
        
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

spirallyTraverse(matrix,3,3)

