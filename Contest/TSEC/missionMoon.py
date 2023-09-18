if __name__ == "__main__":
    t = int(input().strip())
    while t:
        # Read N, M, and H
        n, m, h = map(int, input().strip().split())

        # Read energy capacities of cars
        a = list(map(int, input().strip().split()))

        # Read power of power outlets
        b = list(map(int, input().strip().split()))

        ans = 0

        # Sort the cars and power outlets in descending order
        a.sort(reverse=True)
        b.sort(reverse=True)

        for i in range(min(n, m)):
            ans += min(b[i] * h, a[i])

        print(ans)
        t -= 1
