okdef nextGreaterPermutation(A):
    n = len(A)
    ind = -1
    for i in range(n-2, -1,-1):
        if A[i] < A[i+1]:
            ind = i
            break
    if ind == -1:
        A.reverse()
        return A
    
    for i in range(n-1, ind, -1):
        if A[i] > A[ind]:
            A[i],A[ind] = A[ind],A[i]
            break
            
    # Step 3: reverse the right half:
    A[ind+1:] = reversed(A[ind+1:])
    print(A[ind+1:])
    
    return A

if __name__=="__main__":
    # print(nextGreaterPermutation([1,2,3]))
    print(nextGreaterPermutation([2,1,5,4,3,0,0]))