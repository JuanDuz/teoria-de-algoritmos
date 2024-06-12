def ford_fulkerson(graph, s, t):  # O(V * E**2) con bfs
    flow = {}
    for v in graph.vertices():
        for w in graph.adjacents(v):
            flow[(v, w)] = 0

    grafo_residual = graph
    path = grafo_residual.bfs(s, t)
    while path is not None:
        augment(flow, path, graph)
        path = grafo_residual.bfs(s, t)

    max_flow = 0
    for edge, value in flow.items():
        if edge[0] == 0:
            max_flow += value

    return flow, max_flow


def bottleneck(graph, path):
    bottleneck_val = float('inf')
    for i in range(len(path) - 1):
        bottleneck_val = min(graph.weights[path[i]][path[i + 1]], bottleneck_val)
    return bottleneck_val


def augment(f, path, residual_graph):
    bottleneck_val = bottleneck(residual_graph, path)
    for i in range(1, len(path)):
        if path[i] in residual_graph.adjacents(path[i - 1]):
            f[(path[i - 1], path[i])] += bottleneck_val
            update_residual_graph(residual_graph, path[i - 1], path[i], bottleneck_val)
        else:
            f[(path[i], path[i - 1])] -= bottleneck_val
            update_residual_graph(residual_graph, path[i - 1], path[i], bottleneck_val)
    return f


def update_residual_graph(residual_graph, u, v, bottleneck_val):
    before_weight = residual_graph.weights[u][v]
    if before_weight == bottleneck_val:
        residual_graph.remove_edge(u, v)
    else:
        residual_graph.weights[u][v] = before_weight - bottleneck_val
    if not residual_graph.are_adjacent(v, u):
        residual_graph.add_edge(v, u, bottleneck_val)
    else:
        residual_graph.weights[v][u] = before_weight + bottleneck_val
