import networkx as nx

import heapq

from load import graph
from draw import draw


def dijkstra_nx(g, start_node, target_node):
    dijkstra_path = list(nx.dijkstra_path(g, source=start_node, target=target_node))
    print(f"Dijkstra path between {start_node} and {target_node}: {dijkstra_path}")

    dijkstra_edges = [(dijkstra_path[i], dijkstra_path[i + 1]) for i in range(len(dijkstra_path) - 1)]

    edge_weights = nx.get_edge_attributes(g, 'weight')
    edge_weights_str = {edge: f"{weight:.2f}" for edge, weight in edge_weights.items()}

    draw(g, title=f'Les Miserables: Dijkstra path from {start_node} to {target_node}',
         highlighted_edges=dijkstra_edges, edge_labels=edge_weights_str)


def dijkstra(g, start_node, target_node):
    priority_queue = [(0, start_node)]

    shortest_distances = {node: float('infinity') for node in g}
    shortest_distances[start_node] = 0

    predecessors = {node: None for node in g}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == target_node:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = predecessors[current_node]
            return path, shortest_distances[target_node]

        for neighbor, params in g[current_node].items():
            distance = current_distance + params['weight']
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return [], float('infinity')


def main():
    print("Using NetworkX:")
    dijkstra_nx(graph, 'Dahlia', 'MotherPlutarch')

    print("\nUsing own Dijkstra realization:")
    path = dijkstra(graph, 'Dahlia', 'MotherPlutarch')
    print(f"Dijkstra path between Dahlia and MotherPlutarch: {path[0]}")


if __name__ == '__main__':
    main()
