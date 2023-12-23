import networkx as nx

from load import graph
from draw import draw


def bfs_nx(g, start_node):
    bfs_path = list(nx.bfs_edges(g, source=start_node))

    draw(g, title=f'Les Miserables: Breadth-First Search from {start_node}', highlighted_edges=bfs_path)


def bfs(g, start_node):
    queue = [(start_node, None)]
    visited = set()
    forward_edges = []

    while queue:
        current_node, predecessor = queue.pop(0)

        if current_node not in visited:
            visited.add(current_node)

            if predecessor is not None:
                forward_edges.append((predecessor, current_node))

            neighbors = list(g.neighbors(current_node))
            for neighbor in neighbors:
                queue.append((neighbor, current_node))

    return forward_edges


def main():
    bfs_nx(graph, 'Valjean')


if __name__ == '__main__':
    main()
