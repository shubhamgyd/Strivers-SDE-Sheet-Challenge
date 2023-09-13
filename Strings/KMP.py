def longProperPrefixSuffix(str, n):
    for len in range(n-1, -1, -1):
        count = -1
        for j in range(len):
            if str[j] != str[n - len + j]:
                break
            count += 1
        if(count == len-1):
        # else:
            return len
    return 0 

def fillLPS(str, lps):
    lps[0] = 0
    for i in range(1, len(str)):
        lps[i] = longProperPrefixSuffix(str, i + 1)
    return lps
        
str = "abacabad"
lps = [-1 for i in range(len(str))]
lps = fillLPS(str, lps)
print(lps)