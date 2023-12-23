import unittest

import networkx as nx

from load import graph
from dfs import dfs


class TestDFS(unittest.TestCase):
    def test_dfs(self):
        for node in list(graph.nodes()):
            nx_dfs_path = list(nx.dfs_edges(graph, node))
            dfs_path = dfs(graph, node)

            self.assertEqual(nx_dfs_path, dfs_path)


if __name__ == '__main__':
    unittest.main()
