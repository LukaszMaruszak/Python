from Graph import Graph, Edge
from visualization import plot_Graph, plot_Mst


# odczytanie pliku, w którym zapisany jest wygląd grafu
def load_file(file_name = 'grafy/graf.txt'):
    file = open(file_name, "r")
    g = Graph()
    for line in file:
        a, b, weight = line.split()
        g.add_edge_undirected(Edge(a, b, weight))
    file.close()
    return g


if __name__ == '__main__':
    graf = load_file("grafy/graf1.txt")
    mst = graf.kruskal_algorithm()

    # wypisanie odczytanego grafu w konsoli
    graf.print_graph()
    # wypisanie w konsoli Minimalnego Drzewa Rozpinającego
    mst.print_graph()

    # stworzenie wzizualizacji wyników działania algorytmu
    plot_Graph(graf)
    plot_Mst(graf, mst)

    graf = load_file()
    mst = graf.kruskal_algorithm()

    # wypisanie odczytanego grafu w konsoli
    graf.print_graph()
    # wypisanie w konsoli Minimalnego Drzewa Rozpinającego
    mst.print_graph()

    # stworzenie wzizualizacji wyników działania algorytmu
    plot_Graph(graf)
    plot_Mst(graf, mst)
