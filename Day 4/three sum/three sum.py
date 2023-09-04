


def triplet(n, arr):
    st = set()

    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            # Calculate the 3rd element:
            third = -(arr[i] + arr[j])

            # Find the element in the set:
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])

    # store the set in the answer:
    ans = list(st)
    return ans


# arr = [1, 3, 3, 2, 1, 4]
arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(n, arr)
if len(ans) == 0:
    print(-1)
else:
    for it in ans:
        print("[", end="")
        for i in it:
            print(i, end=" ")
        print("]", end=" ")
print()

