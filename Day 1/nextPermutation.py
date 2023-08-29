def nextGreaterPermutation(A):
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
            
    # Step 3: reverse the right half:
    A[ind+1:] = reversed(A[ind+1:])
    
    return A

if __name__=="__main__":
    print(nextGreaterPermutation([1,2,3]))