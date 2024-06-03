import unittest
import sys
import os
from models.Graph import Graph

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DegreesTests(unittest.TestCase):
    def setUp(self):
        self.graphThreeNodes = Graph(3)

    def test_degrees_no_edges(self):
        # Тестирование функции degrees() при отсутствии ребер
        self.graphThreeNodes.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(self.graphThreeNodes.degrees(), [0, 0, 0])

    def test_degrees_some_edges(self):
        # Тестирование функции degrees() при наличии некоторых ребер
        self.graphThreeNodes.matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        self.assertEqual(self.graphThreeNodes.degrees(), [2, 2, 2])

    def test_degrees_all_edges(self):
        # Тестирование функции degrees() при наличии всех ребер
        self.graphThreeNodes.matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(self.graphThreeNodes.degrees(), [3, 3, 3])

    def disconnected_graph(self):
        #тестирование функции degrees() при 2х несвязных графов
        self.graphThreeNodes.matrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        self.assertEqual(self.graphThreeNodes.degrees(), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
