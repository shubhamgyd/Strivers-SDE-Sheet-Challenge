def majorityElement(v: [int]) -> [int]:
    cnt1 = 0
    cnt2 = 0
    ele1 = float('-inf')
    ele2 = float('-inf')
    for i in range(len(v)):
        if(cnt1 == 0 and v[i] != ele2):
            cnt1 = 1
            ele1 = v[i]
        elif(cnt2==0 and v[i] != ele1):
            cnt2 = 1
            ele2 = v[i]
        elif(ele1 == v[i]):
            cnt1 += 1
        elif(ele2 == v[i]):
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 2

    cnt11 = 0
    cnt22 = 0
    for i in range(len(v)):
        if ele1 == v[i]:
            cnt11 += 1
        if ele2 == v[i]:
            cnt22 += 1
    lens = []
    if cnt11 >= len(v)//3 + 1:
        lens.append(ele1)
    if cnt22 >= len(v)//3 + 1:
        lens.append(ele2)
    return lens

arr = [11, 33, 33, 11, 33, 11]
print(majorityElement(arr))