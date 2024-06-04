import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

GRAPHRORTEST = Graph(5)
GRAPHRORTEST.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])


class PathTests(unittest.TestCase):
    def test_path_exists(self): #Путь существует в графе
        self.assertTrue(GRAPHRORTEST.path(0, 4))
        self.assertTrue(GRAPHRORTEST.path(0, 3))
        self.assertTrue(GRAPHRORTEST.path(1, 4))
        self.assertTrue(GRAPHRORTEST.path(2, 4))

    def test_path_does_not_exist(self): #Путь не существует
        GRAPHRORTEST.add_nodes_from([5])
        self.assertFalse(GRAPHRORTEST.path(0, 5))
        self.assertFalse(GRAPHRORTEST.path(4, 5))
    
    def test_path_to_self(self): #Проверка петли (путь у самому себе)
        self.assertFalse(GRAPHRORTEST.path(0, 0))
        self.assertFalse(GRAPHRORTEST.path(4, 4))
        GRAPHRORTEST.add_edge(0, 0)
        GRAPHRORTEST.add_edge(4, 4)
        self.assertTrue(GRAPHRORTEST.path(0, 0))
        self.assertTrue(GRAPHRORTEST.path(4, 4))
    
    def test_disconnected_graph(self): #Проверяет отдельные компоненты (когда граф не связный)
        GRAPHRORTEST.add_nodes_from([5, 6])
        GRAPHRORTEST.add_edge(5, 6)
        self.assertFalse(GRAPHRORTEST.path(0, 5))
        self.assertFalse(GRAPHRORTEST.path(4, 5))
        self.assertTrue(GRAPHRORTEST.path(5, 6))

if __name__ == '__main__':
    unittest.main()