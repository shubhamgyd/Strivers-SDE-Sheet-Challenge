def print_1_To_N(i,N):
    if i < 1:
        return
    print_1_To_N(i-1,N)
    print(i)

if __name__=="__main__":
    i = 3
    N = 3
    print_1_To_N(i,N)