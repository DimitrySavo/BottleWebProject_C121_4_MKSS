import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

GRAPH_FOR_TEST = Graph(5)
GRAPH_FOR_TEST.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])


GRAPH_FOR_TEST_WITHOUT_LOOP = Graph(5)
GRAPH_FOR_TEST_WITHOUT_LOOP.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4)])

class DfsTests(unittest.TestCase):

    def test_path_exists(self): #Пути существуют
        visited = [False] * GRAPH_FOR_TEST.size
        self.assertTrue(GRAPH_FOR_TEST.dfs(0, 4, visited, 0))
        visited = [False] * GRAPH_FOR_TEST.size
        self.assertTrue(GRAPH_FOR_TEST.dfs(1, 3, visited, 0))

    def test_path_to_self_without_loop(self): #Проверяет что петли нет
        visited = [False] * GRAPH_FOR_TEST_WITHOUT_LOOP.size
        self.assertFalse(GRAPH_FOR_TEST_WITHOUT_LOOP.dfs(0, 0, visited, 0))
        visited = [False] * GRAPH_FOR_TEST_WITHOUT_LOOP.size
        self.assertFalse(GRAPH_FOR_TEST_WITHOUT_LOOP.dfs(4, 4, visited, 0))

    def test_path_does_not_exist(self): #Проверка пути несвязанных вершин
        visited = [False] * GRAPH_FOR_TEST.size
        print(GRAPH_FOR_TEST.size)
        GRAPH_FOR_TEST.add_nodes_from([5])
        self.assertFalse(GRAPH_FOR_TEST.dfs(0, 5, visited, 0))
        visited = [False] * GRAPH_FOR_TEST.size
        self.assertFalse(GRAPH_FOR_TEST.dfs(4, 5, visited, 0))

    def test_path_to_self_with_loop(self): #Существует петля
        visited = [False] * GRAPH_FOR_TEST.size 
        GRAPH_FOR_TEST.add_edge(0, 0)
        self.assertTrue(GRAPH_FOR_TEST.dfs(0, 0, visited, 0))
        visited = [False] * GRAPH_FOR_TEST.size
        GRAPH_FOR_TEST.add_edge(4, 4)
        self.assertTrue(GRAPH_FOR_TEST.dfs(4, 4, visited, 0))

    def test_disconnected_graph(self): #Проверяет несвязанные вершины и связанные в разъединенном графе
        GRAPH_FOR_TEST.add_nodes_from([5, 6])
        GRAPH_FOR_TEST.add_edge(5, 6)
        visited = [False] * GRAPH_FOR_TEST.size
        self.assertFalse(GRAPH_FOR_TEST.dfs(0, 5, visited, 0))
        visited = [False] * GRAPH_FOR_TEST.size
        self.assertFalse(GRAPH_FOR_TEST.dfs(4, 5, visited, 0))
        visited = [False] * GRAPH_FOR_TEST.size
        self.assertTrue(GRAPH_FOR_TEST.dfs(5, 6, visited, 0))

    def test_graph_with_non_affecting_loops(self): #Проверка для влияние петли на поиск пути между другими вершинами
        GRAPH_FOR_TEST.add_edge(1, 1)
        GRAPH_FOR_TEST.add_edge(3, 3)
        visited = [False] * GRAPH_FOR_TEST.size
        self.assertTrue(GRAPH_FOR_TEST.dfs(0, 4, visited, 0))

if __name__ == '__main__':
    unittest.main()