
def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    L[left], L[right] = L[right], L[left]


class Edge:
    """Klasa dla krawędzi z wagą."""
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
        """Konstruktor Grafu. Słownikowa reprezentacja grafu"""
        self.graph = {}

        # zmienne wykorzystywane w algorytmie Kruskala
        self.parent = {}
        self.rank = {}

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
        """Wypisuje postać grafu nieskierowanego ważonego na ekranie."""
        L = []
        for source in self.graph:
            L.append("{} : ".format(source))
            for target in self.graph[source]:
                L.append("{}({}) ".format(target, self.graph[source][target]))
            L.append("\n")
        print("".join(L))

    def sort_edges(self):
        """Sortowanie krawędzi na podstawie ich wagi"""
        L = self.list_edges()
        for i in range(0, len(L) - 1):
            for j in range(0, len(L) - 1):
                if L[j][2] > L[j + 1][2]:
                    swap(L, j + 1, j)
        return L

    def FindParent(self, node):
        """Znajdz Rodzica wierzchołka w grafie"""
        if self.parent[node] == node:
            return node
        return self.FindParent(self.parent[node])

    def Kruskal_Algorithm(self):
        # mst -  minimum spanning tree
        mst = Graph()
        L = self.sort_edges()

        # inicjaliacja słownika zawierającego rodzica każdego węzła
        for n in self.list_nodes():
            # każdy węzeł jest rodzicem dla samego siebie
            self.parent[n] = n
            # każdy węzeł nie jest połączony z innym węzłem
            self.rank[n] = 0

        # przechodę po posortowanej rosnąco liście krawędzi zaczynając od pierwszej
        for j in range(0, len(L)):
            i = L.pop(0)
            # i = Edge(start, koniec, waga)
            start = i[0]
            koniec = i[1]
            waga = i[2]
            rodzic1 = self.FindParent(start)
            rodzic2 = self.FindParent(koniec)
            # Sprawdzam czy do drzewa rozpinającego dodałem wszystkie krawędzie z grafu

            # kiedy rodzice węzła początkowego i końcowego krawędzi są w inny zbiorze
            # dodaje do mst
            if rodzic1 != rodzic2:
                mst.add_edge_undirected(Edge(start, koniec, waga))
                # łączę dwa zbiory do większego dodaje mniejszy
                # dodanie zbiorów to aktualizacja rodzica w słowniku parent
                if self.rank[rodzic1] < self.rank[rodzic2]:
                    self.parent[rodzic1] = rodzic2
                    self.rank[rodzic2] += 1
                else:
                    self.parent[rodzic2] = rodzic1
                    self.rank[rodzic1] += 1
        return mst
