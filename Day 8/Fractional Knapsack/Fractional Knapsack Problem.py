def FractionalKanpsack(values, weight, w):
    d = dict()
    d1 = dict()
    n = len(values)
    
    
    for i in range(n):
        d[values[i]] = values[i]/weight[i]
        d1[weight[i]] = values[i]/weight[i]
    
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    sorted_d1 = sorted(d1.items(), key=lambda x: x[1], reverse=True)
    
    
    l = 0
    total = 0
    i = 0
    while total < w:
        if total + sorted_d1[i][0] < w:
            total += sorted_d1[i][0]
            l += (sorted_d[i][0])
            i += 1
        else:
            x = sorted_d1[i][0]/(w - total)
            total += (sorted_d1[i][0])//x
            l += (sorted_d[i][0]/x)
            i += 1
    return l
    
values = [100, 60, 120]
weight = [20, 10, 30]
w = 50
print(FractionalKanpsack(values, weight, w))

# Time Complexity: O(N * logN) + O(N)

# Space Complexity: O(N + N)