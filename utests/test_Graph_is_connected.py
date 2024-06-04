import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

class IsConnectedTests(unittest.TestCase):
    def test_connected_graph(self): #Проверка на связность
        graph = Graph(5)
        graph.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])
        self.assertTrue(graph.is_connected())

    def test_disconnected_graph(self): #проверка на несвязность
        graph = Graph(5)
        graph.add_edges_from([(0, 1), (1, 2)])
        self.assertFalse(graph.is_connected())

    def test_single_node_graph(self): #Граф с 1 вершиной
        graph = Graph(1)
        self.assertTrue(graph.is_connected())

    def test_graph_with_loops(self): #Все вершины соединены сами с собой
        graph = Graph(3)
        graph.add_edges_from([(0, 0), (1, 1), (2, 2)])
        self.assertFalse(graph.is_connected())

    def test_graph_with_isolated_node(self): #1 вершины не связана
        graph = Graph(4) 
        graph.add_edges_from([(0, 1), (1, 2)])
        self.assertFalse(graph.is_connected())

if __name__ == '__main__':
    unittest.main()