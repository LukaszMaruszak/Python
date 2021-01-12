class Edge:
    """Klasa dla krawędzi skierowanej z wagą."""

    def __init__(self, source, target, weight=1):
        """Konstruktor krawędzi."""
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Zwraca reprezentację napisową krawędzi."""
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.source), repr(self.target))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.source), repr(self.target), repr(self.weight))


class Graph:
    def __init__(self):
        """Konstruktor krawędzi."""
        self.graph = {}

    def add_node(self, node):
        """Wstawia wierzchołek do grafu."""
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge_undirected(self, edge):
        """Dodaje krawędź do grafu nieskierowanego."""
        source = edge.source
        weight = edge.weight
        target = edge.target

        self.add_node(source)
        self.add_node(target)
        # Możemy wykluczyć pętle.
        if source == target:
            raise ValueError("pętle są zabronione")
        if target not in self.graph[source]:
            self.graph[source][target] = weight
        if source not in self.graph[target]:
            self.graph[target][source] = weight

    def list_nodes(self):
        """Zwraca listę wierzchołków grafu."""
        return self.graph.keys()

    def list_edges(self):
        """Zwraca listę krawędzi (3-krotek) grafu skierowanego ważonego."""
        L = []
        for source in self.graph:
            for target in self.graph[source]:
                L.append((source, target, self.graph[source][target]))
        return L

    def print_graph(self):
        """Wypisuje postać grafu skierowanego ważonego na ekranie."""
        L = []
        for source in self.graph:
            L.append("{} : ".format(source))
            for target in self.graph[source]:
                L.append("{}({}) ".format(target, self.graph[source][target]))
            L.append("\n")
        print("".join(L))


g = Graph()
g.add_edge_undirected(Edge("A", 2, 10))
g.add_edge_undirected(Edge(2, "B", 15))
g.add_edge_undirected(Edge(1, 3, 11))

print (g.list_nodes())
print(g.list_edges())
g.print_graph()
