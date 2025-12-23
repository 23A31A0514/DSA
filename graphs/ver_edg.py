def count_vertices_edges(graph):
    vertices = len(graph)
    edges = sum(len(graph[v]) for v in graph) // 2
    return vertices, edges
