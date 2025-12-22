def is_connected(graph):
    visited = set()
    start = list(graph.keys())[0]

    def dfs_check(v):
        visited.add(v)
        for n in graph[v]:
            if n not in visited:
                dfs_check(n)

    dfs_check(start)
    return len(visited) == len(graph)
