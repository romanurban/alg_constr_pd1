def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    raw = data[1:]
    edges = []
    for i in range(0, len(raw), 3):
        a = int(raw[i])
        b = int(raw[i + 1])
        w = int(raw[i + 2])
        edges.append((w, a, b))
    
    # Aprēķināt visu šķautņu svaru summu
    total_weight = sum(w for w, _, _ in edges)
    
    # Sakārtot šķautnes dilstošā svaru secībā
    edges.sort(reverse=True)
    
    # Inicializēt MST blakusvirsotņu sarakstu
    mst_adj = [[] for _ in range(n + 1)]
    mst_weight = 0
    in_mst = [False] * len(edges)
    
    def dfs(a, b, visited):
        if a == b:
            return True
        visited[a] = True
        for v in mst_adj[a]:
            if not visited[v]:
                if dfs(v, b, visited):
                    return True
        return False
    
    # Veidojam MST, izmantojot DFS ciklu pārbaudei
    for idx, (w, a, b) in enumerate(edges):
        visited = [False] * (n + 1)
        if not dfs(a, b, visited):
            mst_adj[a].append(b)
            mst_adj[b].append(a)
            mst_weight += w
            in_mst[idx] = True
    
    # Aprēķināt neiekļautu šķautņu kopējo svaru
    W = total_weight - mst_weight
    # Malas, kas nav iekļautas MST
    chosen = [(edges[i][1], edges[i][2]) for i in range(len(edges)) if not in_mst[i]]
    
    # Izvade: k W a1 b1 a2 b2 ... ak bk
    print(len(chosen), W, end='')
    for a, b in chosen:
        print(f' {a} {b}', end='')
    print()
    
if __name__ == '__main__':
    main()