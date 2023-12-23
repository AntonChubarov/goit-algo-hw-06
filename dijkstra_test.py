import unittest

import networkx as nx

from load import graph
from dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        nodes = list(graph.nodes())

        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j:
                    nx_dijkstra_path_length = nx.dijkstra_path_length(graph, nodes[i], nodes[j])
                    dijkstra_path = dijkstra(graph, nodes[i], nodes[j])

                    self.assertEqual(nx_dijkstra_path_length, dijkstra_path[1])


if __name__ == '__main__':
    unittest.main()
