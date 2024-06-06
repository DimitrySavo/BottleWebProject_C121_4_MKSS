import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

class TestCountIsolatedSubgraphs(unittest.TestCase):
    def test_count_isolated_subgraphs(self):
        # Тест 1: Граф с 1 узлом и без ребер
        graph1 = Graph(1)
        graph1.add_edges_from([])
        self.assertEqual(graph1.count_isolated_subgraphs(), 1)

        # Тест 2: Граф с 4 узлами и без ребер
        graph2 = Graph(4)
        graph2.add_edges_from([])
        self.assertEqual(graph2.count_isolated_subgraphs(), 4)

        # Тест 3: Граф с 4 узлами и некоторыми ребрами
        graph3 = Graph(4)
        graph3.add_edges_from([[0, 1], [2, 3]])
        self.assertEqual(graph3.count_isolated_subgraphs(), 2)

        # Тест 4: Полный граф с 4 узлами
        graph4 = Graph(4)
        graph4.add_edges_from([[i, j] for i in range(4) for j in range(i+1, 4)])
        self.assertEqual(graph4.count_isolated_subgraphs(), 1)

        # Тест 5: Граф с 6 узлами и изолированными парами
        graph5 = Graph(6)
        graph5.add_edges_from([[0, 1], [2, 3], [4, 5]])
        self.assertEqual(graph5.count_isolated_subgraphs(), 3)
        
        # Тест 6: Граф с 6 узлами 
        # Матрица смежности:
        # [0, 0, 0, 0, 0, 0]
        # [0, 0, 1, 1, 0, 0]
        # [0, 1, 0, 1, 0, 0]
        # [0, 1, 1, 0, 0, 0]
        # [0, 0, 0, 0, 0, 1]
        # [0, 0, 0, 0, 0, 1]
        graph6 = Graph(6)
        graph6.add_edges_from([
            [1, 2], [1, 3], 
            [2, 1], [2, 3], 
            [3, 1], [3, 2], 
            [4, 5], [5, 4]
        ])
        self.assertEqual(graph6.count_isolated_subgraphs(), 3)

if __name__ == '__main__':
    unittest.main()
