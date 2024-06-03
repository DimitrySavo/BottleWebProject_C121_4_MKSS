import unittest
import sys
import os
from models.Graph import Graph

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class IsRegularTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(3)

    def test_regular_graph(self):
        # Проверяем, является ли граф правильным
        self.graph.matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        self.assertEqual(self.graph.is_regular(3), "Правильный")

    def test_non_regular_graph(self):
        # Проверяем, является ли граф неправильным
        self.graph.matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        self.assertEqual(self.graph.is_regular(3), "Не правильный")

    def test_incorrect_number_of_vertices(self):
        # Проверяем, обрабатывается ли неверное число вершин
        self.graph.matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        self.assertEqual(self.graph.is_regular(2), "Неверное число вершин")

if __name__ == '__main__':
    unittest.main()
