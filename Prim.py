INF = 9999999
V = 5
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

def prim_mst(graph):
    selected = [False] * V
    # Start with the first vertex (0)
    selected[0] = True
    no_edge = 0
    
    print("Edge : Weight")
    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0
        
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        
        print(f"{x}-{y}: {graph[x][y]}")
        selected[y] = True
        no_edge += 1

if __name__ == "__main__":
    prim_mst(G)
