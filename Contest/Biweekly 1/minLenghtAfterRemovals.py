def test(a):
    d = dict()
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    k = d.items()
    print(k)
    
arr = [1, 1, 2, 2, 3, 3]
test(arr)