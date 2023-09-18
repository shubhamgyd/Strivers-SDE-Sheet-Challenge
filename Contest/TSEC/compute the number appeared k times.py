def compute(k,s,n):
    l = []
    count = n
    for i in range(1,10000):
        if i % 2 != 0:
            count -= 1
            l.append(i)
        if count == 0:
            break
    len_of_array = (n  - 1) + k
    t = len_of_array
    for i in l:
        if i*k < s:
            t -= k
            temp = l.copy()
            target = s - i*k
            temp.remove(i)
            if len_of_array == k:
                return i
            elif len_of_array > k:
                count1 = t
                for j in temp:
                    count1 -= 1
                    target -= j
                    if count1== 0:
                        break
                    if target == 0:
                        return i
    return 1
    
        
if __name__=="__main__":
    t=int(input())
    while t:
        string_input = list(input().strip().split())
        n = string_input[0]
        k = string_input[1]
        s = string_input[2]
        print(compute(int(k),int(s),int(n)))
        t -= 1