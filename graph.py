import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colormaps


def draw(graph, title=None, highlighted_edges=None, edge_labels=None):
    degree_dict = dict(graph.degree())
    degrees = list(degree_dict.values())

    colormap = colormaps.get_cmap('cool')

    node_colors = [colormap(d / max(degrees)) for d in degrees]

    plt.figure(figsize=(16, 9))

    if title:
        plt.title(title)

    pos = nx.spring_layout(graph, k=0.3, iterations=100)

    nx.draw(graph, pos, node_size=100, node_color=node_colors, edge_color='#808080', width=0.5, with_labels=True,
            font_size=8)

    if highlighted_edges:
        nx.draw_networkx_edges(graph, pos, edgelist=highlighted_edges, edge_color='red', width=0.5)

    if edge_labels:
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

    plt.show()


def bfs(graph, start_node):
    bfs_path = list(nx.bfs_edges(graph, source=start_node))

    draw(graph, title=f'Les Miserables: Breadth-First Search from {start_node}', highlighted_edges=bfs_path)


def dfs(graph, start_node):
    dfs_path = list(nx.dfs_edges(graph, source=start_node))

    draw(graph, title=f'Les Miserables: Depth-First Search from {start_node}', highlighted_edges=dfs_path)


def dijkstra(graph, start_node, target_node):
    dijkstra_path = list(nx.dijkstra_path(graph, source=start_node, target=target_node))
    print(f"\nDijkstra path between {start_node} and {target_node}: {dijkstra_path}")

    dijkstra_edges = [(dijkstra_path[i], dijkstra_path[i + 1]) for i in range(len(dijkstra_path) - 1)]

    edge_weights = nx.get_edge_attributes(graph, 'weight')
    edge_weights_str = {edge: f"{weight:.2f}" for edge, weight in edge_weights.items()}

    draw(graph, title=f'Les Miserables: Dijkstra path from {start_node} to {target_node}',
         highlighted_edges=dijkstra_edges, edge_labels=edge_weights_str)


def main():
    gml_file_path = './data/lesmis.gml'

    print('Les Miserables graph\n')

    graph = nx.read_gml(gml_file_path)

    print("Nodes:", graph.number_of_nodes())
    print("Edges:", graph.number_of_edges())

    degree_dict = dict(graph.degree())

    sorted_nodes = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)

    # Display the top 5 nodes by degree
    top_nodes = sorted_nodes[:5]
    print("\nTop 5 nodes by degree:")
    for node, degree in top_nodes:
        print(f"{node}: {degree}")

    draw(graph, title='Les Miserables characters interaction')

    bfs(graph, 'Valjean')

    dfs(graph, 'Valjean')

    # Add edge weights: as edge value is the level of coappearance, let's make the weight as 1 / value
    for u, v, d in graph.edges(data=True):
        d['weight'] = 1 / d['value']

    dijkstra(graph, 'Dahlia', 'MotherPlutarch')


if __name__ == '__main__':
    main()
