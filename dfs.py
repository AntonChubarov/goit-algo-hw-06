import networkx as nx

from load import graph
from draw import draw


def dfs_nx(g, start_node):
    dfs_path = list(nx.dfs_edges(g, source=start_node))

    draw(g, title=f'Les Miserables: Depth-First Search from {start_node}', highlighted_edges=dfs_path)


def dfs(g, start_node):
    visited = set()
    forward_edges = []

    def dfs_internal(node):
        visited.add(node)
        for neighbor in g[node]:
            if neighbor not in visited:
                forward_edges.append((node, neighbor))
                dfs_internal(neighbor)

    dfs_internal(start_node)

    return forward_edges


def main():
    dfs_nx(graph, 'Valjean')


if __name__ == '__main__':
    main()
