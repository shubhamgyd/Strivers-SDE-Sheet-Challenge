def isSafe():
    pass

def solve(node, color, m, N, graph):
    if node == N:
        return True
    
    for i in range(1, m+1):
        if isSafe(node, color, graph, N, i)

def graphColoring():
    pass

if __name__=="__main__":
    N = 4
    m = 3
    
    
    graph = [[0 for i in range(3)] for j in range(3)]
    
    # Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1


    print(1 if graphColoring(graph, m, N) else 0)