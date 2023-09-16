def N_Meetings(start, end):
    l = []
    n = len(start)
    l = [[end[i], start[i]] for i in range(n)]
    l.sort()
    temp = [1]
    meeting = l[0][0]
    for i in range(1,n):
        if l[i][1] >  meeting:
            meeting = l[i][0]
            temp.append(i+1)
    
    print("The order in which these meetings will be performed are: ")
    for i in range(len(temp)):
        print(temp[i], end=' ')
            
    
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]
N_Meetings(start, end)