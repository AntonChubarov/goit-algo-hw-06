import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colormaps


def bfs(graph, start_node):
    # Perform BFS
    bfs_path = list(nx.bfs_edges(graph, source=start_node))

    degree_dict = dict(graph.degree())
    degrees = list(degree_dict.values())

    # Visualize the graph with BFS path highlighted
    colormap = colormaps.get_cmap('cool')

    # Assign colors to nodes based on their degree
    node_colors = [colormap(d / max(degrees)) for d in degrees]

    plt.figure(figsize=(16, 9))
    plt.title('Breadth-First Search')

    pos = nx.spring_layout(graph, k=0.3, iterations=100)
    nx.draw(graph, pos, node_size=100, node_color=node_colors, edge_color='#808080', width=0.5, with_labels=True,
            font_size=8)

    nx.draw_networkx_edges(graph, pos, edgelist=bfs_path, edge_color='red', width=0.5)

    plt.show()


def dfs(graph, start_node):
    # Perform DFS
    dfs_path = list(nx.dfs_edges(graph, source=start_node))

    degree_dict = dict(graph.degree())
    degrees = list(degree_dict.values())

    # Visualize the graph with DFS path highlighted
    colormap = colormaps.get_cmap('cool')

    # Assign colors to nodes based on their degree
    node_colors = [colormap(d / max(degrees)) for d in degrees]

    plt.figure(figsize=(16, 9))
    plt.title('Depth-First Search')

    pos = nx.spring_layout(graph, k=0.3, iterations=100)
    nx.draw(graph, pos, node_size=100, node_color=node_colors, edge_color='#808080', width=0.5, with_labels=True,
            font_size=8)

    nx.draw_networkx_edges(graph, pos, edgelist=dfs_path, edge_color='red', width=0.5)

    plt.show()


def dijkstra(graph, start_node, target_node):
    # Perform Dijkstra
    dijkstra_path = list(nx.dijkstra_path(graph, source=start_node, target=target_node))
    print(f"\nDijkstra path between {start_node} and {target_node}: {dijkstra_path}")

    dijkstra_edges = [(dijkstra_path[i], dijkstra_path[i + 1]) for i in range(len(dijkstra_path) - 1)]

    degree_dict = dict(graph.degree())
    degrees = list(degree_dict.values())

    # Visualize the graph with Dijkstra path highlighted
    colormap = colormaps.get_cmap('cool')

    # Assign colors to nodes based on their degree
    node_colors = [colormap(d / max(degrees)) for d in degrees]

    plt.figure(figsize=(16, 9))
    plt.title('Dijkstra')

    pos = nx.spring_layout(graph, k=0.3, iterations=100)
    nx.draw(graph, pos, node_size=100, node_color=node_colors, edge_color='#808080', width=0.5, with_labels=True,
            font_size=8)

    nx.draw_networkx_edges(graph, pos, edgelist=dijkstra_edges, edge_color='red', width=0.5)

    edge_weights = nx.get_edge_attributes(graph, 'weight')

    edge_weights_str = {edge: f"{weight:.2f}" for edge, weight in edge_weights.items()}

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weights_str, font_size=6)

    plt.show()


def main():
    gml_file_path = './data/lesmis.gml'

    graph = nx.read_gml(gml_file_path)

    print("Nodes:", graph.number_of_nodes())
    print("Edges:", graph.number_of_edges())

    # Get the degree of each node
    degree_dict = dict(graph.degree())
    degrees = list(degree_dict.values())

    # Sort nodes by degree in descending order
    sorted_nodes = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)

    # Display the top 5 nodes by degree
    top_nodes = sorted_nodes[:5]
    print("\nTop 5 nodes by degree:")
    for node, degree in top_nodes:
        print(f"{node}: {degree}")

    # Create a colormap based on node degrees
    colormap = colormaps.get_cmap('cool')

    # Assign colors to nodes based on their degree
    node_colors = [colormap(d / max(degrees)) for d in degrees]

    plt.figure(figsize=(16, 9))
    plt.title('Les Miserables')

    pos = nx.spring_layout(graph, k=0.3, iterations=100)
    nx.draw(graph, pos, node_size=100, node_color=node_colors, edge_color='#808080', width=0.5, with_labels=True,
            font_size=8)

    plt.show()

    bfs(graph, 'Valjean')

    dfs(graph, 'Valjean')

    for u, v, d in graph.edges(data=True):
        d['weight'] = 1 / d['value']

    dijkstra(graph, 'Dahlia', 'MotherPlutarch')


if __name__ == '__main__':
    main()
