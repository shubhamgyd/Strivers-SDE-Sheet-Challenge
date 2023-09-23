if __name__=="__main__":
    n = int(input())
    m = int(input())
    adj = [[] for i in range(m)]
    for i in range(m):
        u = int(input())
        v = int(input())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(m):
        print(adj[i])