def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    L[left], L[right] = L[right], L[left]


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
        # if source not in self.graph[target]:
        #     self.graph[target][source] = weight

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

    def graph_size(self):
        return len(self.list_nodes())

    def print_graph(self):
        """Wypisuje postać grafu skierowanego ważonego na ekranie."""
        L = []
        for source in self.graph:
            L.append("{} : ".format(source))
            for target in self.graph[source]:
                L.append("{}({}) ".format(target, self.graph[source][target]))
            L.append("\n")
        print("".join(L))

    def sort_edges(self):
        L = self.list_edges()
        for i in range(0, len(L) - 1):
            for j in range(0, len(L) - 1):
                if L[j][2] > L[j + 1][2]:
                    swap(L, j + 1, j)
        return L

    def Kruskal_Algorithm(self):
        mst = Graph()
        L = self.sort_edges()
        for j in range(0, len(L)):
            i = L.pop(0)
            # print("Min krawędż" + str(i))
            # Sprawdzam czy do drzewa rozpinającego dodałem wszystkie krawędzie z grafu

            if i[0] not in mst.list_nodes() or i[1] not in mst.list_nodes():
                # print("Not in mst")
                mst.add_edge_undirected(Edge(i[0], i[1], i[2]))
                # print(mst.list_nodes())
                # print("in mst")
            # print("mst size " + str(mst.graph_size() ))
            if mst.graph_size() == self.graph_size():
                return mst



g = Graph()
g.add_edge_undirected(Edge("A", "B", 1))
g.add_edge_undirected(Edge("A", "C", 2))
g.add_edge_undirected(Edge("B", "C", 3))
g.add_edge_undirected(Edge("C", "D", 5))
g.add_edge_undirected(Edge("D", "B", 4))
g.add_edge_undirected(Edge("E", "C", 7))
g.add_edge_undirected(Edge("F", "A", 5))
g.Kruskal_Algorithm().print_graph()
