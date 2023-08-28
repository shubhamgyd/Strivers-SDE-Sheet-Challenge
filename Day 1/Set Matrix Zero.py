def setZero(matrix, n, m):
    temp = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                temp.append([i,j])
    for i in range(len(temp)):
        index1 = temp[i]
        l = index1[0]
        k = index1[1]
        for i in range(n):
            matrix[i][k] = 0
        for i in range(m):
            matrix[l][i] = 0
            
matrix = [[2,4,3],[1,0,0]]
setZero(matrix,2,3)
print(matrix)