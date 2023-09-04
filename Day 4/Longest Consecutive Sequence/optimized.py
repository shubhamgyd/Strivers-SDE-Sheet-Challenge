def longestConsecutiveSequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    longest = 1
    st = set()
    for i in range(n):
        st.add(arr[i])
    
    for it in st:
        if ((it - 1) not in st):
            cnt = 1
            x = it
            while (x + 1) in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

if __name__=="__main__":
    arr = [5, 8, 3, 2, 1, 4]
    print(longestConsecutiveSequence(arr))