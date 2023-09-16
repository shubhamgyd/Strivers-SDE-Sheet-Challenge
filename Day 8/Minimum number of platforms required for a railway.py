def minimumPlatforms(arr, dep):
    platformRequired = 1
    n = len(arr)
    l = [[arr[i],dep[i]] for i in range(n)]
    l.sort()
    dept = [l[0][1]]
    for i in range(1,n):
        for j in range(len(dept)):
            if l[i][0] >= dept[j]:
                dept[j] = l[i][1]
                break
            else:
                dept.append(l[i][1])
                platformRequired += 1
                break
        dept.sort() 
    return platformRequired
    
# arr = [900, 945, 955, 1100, 1500, 1800]
# dep = [920, 1200, 1130, 1150, 1900, 2000]
# arr = [41, 1616, 297, 2042, 1013, 987, 2050, 525, 636, 109]
# dep = [2275, 2076, 1580, 2144, 1231, 1672, 2137, 1016, 2234, 1043]
# arr = [765, 642, 2076]
# dep = [790, 1494, 2087] 
# arr = [768]
# dep = [1119]
arr = [775, 494, 252, 1680] 
dep = [2052, 2254, 1395, 2130]  
print(minimumPlatforms(arr, dep))