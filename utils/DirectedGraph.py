from collections import defaultdict, deque


class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = defaultdict(lambda: defaultdict(int))
        self.value = defaultdict(int)
        self.le_value = defaultdict(int)

    def add_edge(self, u, v, w, vu=0, vv=0, ovu=0, ovv=0):
        self.graph[u].append(v)
        self.weights[u][v] = w
        self.value[u] = vu
        self.value[v] = vv
        self.le_value[u] = ovu
        self.le_value[v] = ovv

    def remove_edge(self, u, v):
        if v in self.graph[u]:
            self.graph[u].remove(v)
            del self.weights[u][v]

    def vertices(self):
        return self.graph.keys()

    def edges(self):
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                edges.append((u, v, self.weights[u][v]))
        return edges

    def adjacents(self, u):
        return self.graph[u]

    def are_adjacent(self, u, v):
        return v in self.graph[u]

    def bfs(self, s, t):
        parents = {}
        visited = set()
        order = {}
        queue = deque([s])
        visited.add(s)
        parents[s] = None
        order[s] = 0
        queue.append(s)

        while queue:
            v = queue.popleft()

            for w in self.graph[v]:
                if w not in visited:
                    visited.add(w)
                    parents[w] = v
                    order[w] = order.get(v) + 1
                    queue.append(w)

                    if w == t:
                        # Reconstruir el camino desde s hasta t
                        path = []
                        current = t
                        while current is not None:
                            path.append(current)
                            current = parents[current]
                        path.reverse()
                        return path
        return None
