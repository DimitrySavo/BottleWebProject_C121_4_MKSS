import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

graph_for_test_small_size = Graph(1)
graph_for_test_small_size.add_edges_from([[0,0]])
graph_for_test_big_size = Graph(8)
graph_for_test_big_size.add_edges_from([[0,0], [0,1], [1,0], [1,1], [1,3], [3,1], [3,6], [3,7], [4,2], [4,4], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [7,7]])
graph_for_test_maximum_size = Graph(10)
graph_for_test_maximum_size.add_edges_from([[0,0], [0,1], [1,0],[1,2], [2,1], [2,2],[2,9],[3,7], [3,9], [4,4], [4,6], [4,7], [4,8], [5,9], [6,1],[6,4], [6,6], [7,1], [7,3],[7,4],[8,4], [8,8],[8,9], [9,2],[9,3],[9,5], [9,8], [9,9]])

class GetIntersectionTest(unittest.TestCase):
    def test_intersection_of_same_graphs(self):
        #Тест одинаковых графов маленького размера
        second_small_graph = Graph(1)
        second_small_graph.add_edges_from([[0,0]])
        intersection = Graph.intersection(graph_for_test_small_size, second_small_graph)
        edges = intersection.get_edges()
        self.assertEqual(edges, [[0,0]])
        #Тест одинаковых графов большого размера
        second_big_graph = Graph(8)
        second_big_graph.add_edges_from([[0,0], [0,1], [1,0], [1,1], [1,3], [3,1], [3,6], [3,7], [4,2], [4,4], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [7,7]])
        intersection = Graph.intersection(second_big_graph, graph_for_test_big_size)
        edges = intersection.get_edges()
        self.assertEqual(edges, [[0, 0], [0, 1], [1, 0], [1, 1], [1, 3], [1, 5], [2, 4], [2, 5], [3, 1], [3, 5], [3, 6], [3, 7], [4, 2], [4, 4], [4, 5], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [6, 3], [6, 5], [7, 3], [7, 7]])
        #Тест одинаковых графов предельного размера
        second_graph_maximum_size = Graph(10)
        second_graph_maximum_size.add_edges_from([[0,0], [0,1], [1,0], [2,1], [2,2], [3,9], [4,4], [4,6], [4,7], [4,8], [5,9], [6,1], [6,6], [7,1], [7,3], [8,8], [9,2], [9,8], [9,9]])
        intersection = Graph.intersection(second_graph_maximum_size, graph_for_test_maximum_size)
        edges = intersection.get_edges()
        self.assertEqual(edges, [[0, 0], [0, 1], [1, 0], [1, 2], [1, 6], [1, 7],
                                  [2, 1], [2, 2], [2, 9], [3, 7], [3, 9], [4, 4],
                                    [4, 6], [4, 7], [4, 8], [5, 9], [6, 1], [6, 4],
                                      [6, 6], [7, 1], [7, 3], [7, 4], [8, 4], [8, 8],
                                        [8, 9], [9, 2], [9, 3], [9, 5], [9, 8], [9, 9]])

    def test_intersection_of_different_not_empty_graphs(self):
        #Тест графа небольшого размера
        second_small_graph = Graph(1)
        second_small_graph.add_edges_from([])
        intersection = Graph.intersection(graph_for_test_small_size, second_small_graph)
        edges = intersection.get_edges()
        self.assertEqual(edges, [])
        #Первый тест графа большого размера
        second_big_graph = Graph(8)
        second_big_graph.add_edges_from([[1,2], [2,1], [2,3], [3,2], [3,3]])
        intersection = Graph.intersection(second_big_graph, graph_for_test_big_size)
        edges = intersection.get_edges()
        self.assertEqual(edges,[])
        #Второй тест графа большого размера
        second_big_graph = Graph(8)
        second_big_graph.add_edges_from([[1,1], [1,2], [2,1], [1,4], [4,1]])
        intersection = Graph.intersection(second_big_graph, graph_for_test_big_size)
        edges = intersection.get_edges()
        self.assertEqual(edges, [[1, 1]])
        #Первый тест графа максимального размера
        second_graph_maximum_size = Graph(10)
        second_graph_maximum_size.add_edges_from([[0,1],[1,0], [1,1],[1,8],[1,9], [2,3],[2,8],[2,9],
                                                   [3,1],[3,2], [3,5], [3,6], [3,7], [3,8],[3,9],[5,9], [4,1],
                                                     [4,3], [4,5], [4,6], [4,7],[5,3], [6,3], [7,3],
                                                       [7,8], [8,1], [8,2],[8,3], [8,7], [9,1], [9,2], [9,3], [9,5]])
        intersection = Graph.intersection(second_graph_maximum_size, graph_for_test_maximum_size)
        edges = intersection.get_edges()
        self.assertEqual(edges,[[0, 1], [1, 0], [2, 9], [3, 7], [3, 9], [4, 6], [4, 7], [5, 9], 
                                [6, 4], [7, 3], [7, 4], [9, 2], [9, 3], [9, 5]])

    def test_intersection_with_empty_graph(self): #Тест с пустым графом
        second_big_graph = Graph(8)
        second_big_graph.add_edges_from([])
        intersection = Graph.intersection(graph_for_test_big_size, second_big_graph)
        edges = intersection.get_edges()
        self.assertEqual(edges,[])

    def test_intersection_with_different_size_graphs(self):
        #Тесты возвращения ошибок при объединении графов с разными размерами
        second_small_graph = Graph(2)
        with self.assertRaises(ValueError):
            Graph.intersection(graph_for_test_small_size, second_small_graph)

        second_big_graph = Graph(6)
        with self.assertRaises(ValueError):
            Graph.intersection(graph_for_test_big_size, second_big_graph)

        second_large_graph = Graph(11)
        with self.assertRaises(ValueError):
            Graph.intersection(graph_for_test_maximum_size, second_large_graph)

if __name__ == '__main__':
    unittest.main()