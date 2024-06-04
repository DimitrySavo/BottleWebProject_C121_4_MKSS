import unittest
import sys
import os
from models.Graph import Graph

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class IsRegularTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(1)

    def test_graph_of_one_node(self):
        matrixes = self.graph.is_regular(1)
        self.assertEqual(list(matrixes), [[1]])

    def test_graph_of_three_node(self):
        matrixes = self.graph.is_regular(3)
        self.assertEqual(list(matrixes), [((0, 1, 1), (1, 0, 1), (1, 1, 0))])

    def test_graph_of_four_node(self):
        matrixes = self.graph.is_regular(4)
        self.assertEqual(list(matrixes), [((0, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 0, 1, 0)), ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0))])

    def test_graph_of_not_int_size(self):
        matrixes = self.graph.is_regular(1.4)
        self.assertEqual(list(matrixes), [])
    
    def test_graph_set_type(self):
        matrixes = self.graph.is_regular(1.4)
        self.assertNotEqual(matrixes, [])
    

if __name__ == '__main__':
    unittest.main()
