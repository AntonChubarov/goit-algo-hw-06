import unittest

import networkx as nx

from load import graph
from bfs import bfs


class TestBFS(unittest.TestCase):
    def test_bfs(self):
        for node in list(graph.nodes()):
            nx_bfs_path = list(nx.bfs_edges(graph, node))
            bfs_path = bfs(graph, node)

            self.assertEqual(str(nx_bfs_path), str(bfs_path))


if __name__ == '__main__':
    unittest.main()
