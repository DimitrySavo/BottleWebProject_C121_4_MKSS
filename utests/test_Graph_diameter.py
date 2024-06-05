import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

class TestDiameter(unittest.TestCase):
    def test_diameter(self):
        # Тест 1: Граф с 1 узлом и без ребер
        graph1 = Graph(1)
        graph1.add_edges_from([])
        self.assertEqual(graph1.diameter(), 0)

        # Тест 2: Граф с 4 узлами и без ребер
        graph2 = Graph(4)
        graph2.add_edges_from([])
        self.assertEqual(graph2.diameter(), 0)  # Нет связей, граф несвязный

        # Тест 3: Линейный граф с 4 узлами
        graph3 = Graph(4)
        graph3.add_edges_from([[0, 1], [1, 2], [2, 3]])
        self.assertEqual(graph3.diameter(), 3)

        # Тест 4: Полный граф с 4 узлами
        graph4 = Graph(4)
        graph4.add_edges_from([[i, j] for i in range(4) for j in range(i+1, 4)])
        self.assertEqual(graph4.diameter(), 1)

        # Тест 5: Граф с 5 узлами и циклом
        graph5 = Graph(5)
        graph5.add_edges_from([[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]])
        self.assertEqual(graph5.diameter(), 2)

        # Тест 6: Несвязный граф с 4 узлами
        graph6 = Graph(4)
        graph6.add_edges_from([[0, 1], [2, 3]])
        self.assertEqual(graph6.diameter(), 0)  # Граф несвязный

if __name__ == '__main__':
    unittest.main()
