def isPalindrome(s, start, end):
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def func(ind, s, path, ans):
    if(ind == len(s)):
        ans.append(path.copy())
        return
    
    for i in range(ind, len(s)):
        if isPalindrome(s,ind,i):
            path.append(s[ind:i+1])
            func(i+1,s,path,ans)
            path.pop()


def palindromePartitioning(s):
    ans = []
    path = []
    func(0,s,path,ans)
    print(ans)

palindromePartitioning("aabb")