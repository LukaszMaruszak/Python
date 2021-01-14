# libraries
import matplotlib.pyplot as plt
import networkx as nx


def plot_Graph(graph):
    G = nx.Graph()
    for edge in graph.list_edges():
        G.add_edge(edge[0],edge[1],color='#6bb56d',weight=int(edge[2]))

    pos = nx.spring_layout(G)

    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]

    edge_labels = nx.get_edge_attributes(G,'weight')

    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color=colors, width=3)
    plt.title("Graf odczytany z pliku")
    plt.show()

def plot_Mst(graph, mst):
    G = nx.Graph()
    for edge in graph.list_edges():
        if edge in mst.list_edges():
            G.add_edge(edge[0],edge[1],color='#6bb56d',weight=int(edge[2]))
        else:
            G.add_edge(edge[0],edge[1],color='#cfcfcf',weight=int(edge[2]))

    pos = nx.spring_layout(G)

    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]

    edge_labels = nx.get_edge_attributes(G,'weight')

    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color=colors, width=3)
    plt.title("Minimalne drzewo rozpinające")
    plt.show()
